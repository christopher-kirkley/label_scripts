import pdfrw
from reportlab.pdfgen import canvas
import datetime
import json
import os

# get environment variable
LABEL = os.environ.get('LABEL')

def load_json():
    with open('info.json') as f:
        data = json.load(f)
    return data

def create_ipr_overlay(data):
    """
    Create the data that will be overlayed on top
    of the form that we want to fill
    """

    now = datetime.date.today()

    c = canvas.Canvas('simple_form_overlay.pdf')

    c.drawString(190, 600, data['album_name'].upper())
    c.drawString(310, 570, 'X') # Distribution?
    c.drawString(350, 520, 'X') # Owner?
    c.drawString(140, 350, data['artist'].upper())
    if data['artist'].lower().replace(" ", "_") in ["various artist", "various artists"]:
        c.drawString(503, 364, 'X') # Compilation?
    else:
        pass
    c.drawString(500, 350, 'Music') # Music?
    c.drawString(350, 110, 'Sahel Sounds') # Org Name
    c.drawString(210, 70, 'Christopher Kirkley, Owner')
    c.drawString(370, 70, now.strftime("%m-%d-%Y")) # Date


    c.save()

def create_cuesheet_overlay(data):
    """
    Create the data that will be overlayed on top
    of the form that we want to fill
    """

    now = datetime.date.today()

    c = canvas.Canvas('simple_form_overlay.pdf')
    
    c.drawString(263, 667, data['artist'].upper())
    c.drawString(263, 633, data['album_name'].upper())
    c.drawString(263, 600, data['catalog_number'].upper())
    c.drawString(263, 570, data['speed'])
    c.drawString(263, 546, 'none added')
    c.drawString(263, 509, data['genre'])
    for i, track in enumerate(data['a']):
        c.drawString(60, 392-20*i, track['track_number'])
        c.drawString(90, 392-20*i, track['track_name'])
        c.drawString(271, 392-20*i, track['length'])
    for i, track in enumerate(data['b']):
        c.drawString(324, 392-20*i, track['track_number'])
        c.drawString(355, 392-20*i, track['track_name'])
        c.drawString(534, 392-20*i, track['length'])


    c.save()

def merge_pdfs(form_pdf, overlay_pdf, output):
    """
    Merge the specified fillable form PDF with the 
    overlay PDF and save the output
    """
    form = pdfrw.PdfReader(form_pdf)
    olay = pdfrw.PdfReader(overlay_pdf)
    
    for form_page, overlay_page in zip(form.pages, olay.pages):
        merge_obj = pdfrw.PageMerge()
        overlay = merge_obj.add(overlay_page)[0]
        pdfrw.PageMerge(form_page).add(overlay).render()
        
    writer = pdfrw.PdfWriter()
    writer.write(output, form)
    
    
if __name__ == '__main__':
    data = load_json()
    create_ipr_overlay(data)
    merge_pdfs(f'{LABEL}/production/atoz/IPR_FINAL.pdf', 
               'simple_form_overlay.pdf', 
               'ipr.pdf')
    create_cuesheet_overlay(data)
    merge_pdfs(f'{LABEL}/production/atoz/AtoZMedia-Vinyl-Audio-Cue-Sheet-Side-AB.pdf',
               'simple_form_overlay.pdf', 
               'cuesheet.pdf')
    """clean up"""
    
    os.remove('simple_form_overlay.pdf')


