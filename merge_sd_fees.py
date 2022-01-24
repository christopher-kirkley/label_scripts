import pandas as pd
import os
import glob

all_files = glob.glob(os.path.join('', "*.xlsx"))

df = pd.concat((pd.read_excel(f) for f in all_files))

df = df.rename(columns={'CATALOG NUMBER': 'catalog_number',
           'warehousing_fee FROM AUTOCALC': 'net'
          })


df = df.groupby(['catalog_number']).sum().reset_index()


df = df[['catalog_number',
          'net'
         ]]
df['description'] = 'warehousing chargeback from distributor ' + df['catalog_number']
df['catalog_number'] = df['catalog_number'].str[0:2] + '-' + df['catalog_number'].str[2:5]
df['date'] = pd.NaT
df['vendor'] = 'Secretly Distribution'
df['expense_type'] = 'Recoupable'
df['item_type'] = 'Fee'
df['artist_name'] = pd.NaT

df.to_csv('out.csv', index=False)


