#!/home/ck/work_scripts/isrc-generator/venv/bin/python

import os
import json
import pyperclip
import pandas as pd
from pandas.io.clipboard import copy

"""Generate ISRC from the command line."""

def make_settings_file():
    data = {
            'country_code': '',
            'isrc_registrant': '',
            }
    with open('settings.json', 'w') as f:
        json.dump(data, f)
    return f.name

class Isrcs:
    def __init__(self, country_code, isrc_registrant, year, catalog_number, tracks):
        self.country_code = country_code
        self.isrc_registrant = isrc_registrant
        self.year = year
        self.catalog_number = catalog_number
        self.tracks = tracks
        
    def make_isrcs(self):
        self.isrcs = []

        for self.track in range(self.tracks):
            isrc = f'{self.country_code}{self.isrc_registrant}{self.year}{self.catalog_number}{self.track+1:02d}'
            self.isrcs.append(isrc)
        return self.isrcs

    def save_settings(self):
        settings_json = {
                'country_code': self.country_code,
                'isrc_registrant': self.isrc_registrant,
                'year': self.year,
                }
        with open('settings.json', 'w') as f:
            json.dump(settings_json, f)

    def make_csv(self):
        df = pd.DataFrame({
            'track_number': [],
            'isrc': [],
            })
        df['isrc'] = self.make_isrcs()
        df['track_number'] = df.index + 1
        csv = df.to_csv('isrcs.csv', index=False)
        return df

def retrieve_settings():
    if os.path.exists('settings.json') == False:
        file = make_settings_file()
    with open('settings.json', 'r') as f:
        data = json.load(f)
    return data


def main():

    json = retrieve_settings()

    while True:
        i = input(f'Two character country code: [{json["country_code"]}] ')
        if len(i) != 2 and i != '':
            continue
        elif i == '':
            country_code = json['country_code']
            break
        else:
            country_code = i
            break

    while True:
        i = input(f'Registrant of ISRC issuer: [{json["isrc_registrant"]}] ')
        if len(i) != 3 and i != '':
            continue
        elif i == '':
            isrc_registrant = json['isrc_registrant']
            break
        else:
            isrc_registrant = i
            break

    while True:
        i = input(f'Two digit year: ')
        if len(i) != 2:
            continue
        else:
            year = i
            break

    while True:
        i = input(f'Three digit catalog number: ')
        if len(i) != 3:
            continue
        else:
            catalog_number = i
            break

    while True:
        tracks = input('Number of tracks: ')
        try:
            tracks = int(tracks)
            break
        except:
            continue

    isrcs = Isrcs(country_code, isrc_registrant, year, catalog_number, tracks)

    isrcs.save_settings()

    generated_isrcs = isrcs.make_isrcs()

    isrcs.make_csv()

    print('\nOUTPUT:')
    for isrc in generated_isrcs:
        print(isrc) 

    # copy to clipboard
    isrc_string = ""
    for isrc in generated_isrcs:
        isrc_string = isrc_string + isrc + "\n"
    
    return isrc_string
    

if __name__ == '__main__':
    isrcs = main()
    #os.system(f"echo {isrcs} | /usr/bin/xsel -b")
    copy(isrcs)
