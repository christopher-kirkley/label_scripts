import pandas as pd
import sys
from os import listdir
import os

def create_df(file):
    df = pd.read_excel(file, skiprows=4)
    return df

def export_to_csv(df, root):
    df.to_csv(f'{root}.csv', index=False)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cwd = os.getcwd()
        filepaths = [f for f in listdir(cwd) if f.endswith('.xlsx')]
        df = pd.concat((pd.read_excel(f) for f in filepaths))
        df = df[['CATALOG NUMBER', 'warehousing_fee FROM AUTOCALC']]

        df.rename(columns={
            'CATALOG NUMBER': 'catalog_number',
            'warehousing_fee FROM AUTOCALC': 'net'
            },
           inplace=True)

        df = df.groupby(['catalog_number'], as_index=False).sum()

        df['catalog_number'] = (
                df['catalog_number'].str.slice(0,2)
                + '-'
                + df['catalog_number'].str.slice(2,5)
                )

        df['date'] = sys.argv[1]
        df['vendor'] = 'Secretly Distribution'
        df['expense_type'] = 'Recoupable'
        df['item_type'] = 'Fee'
        df['artist_name'] = ''
        df['description'] = 'chargeback/freight charges from distributor ' + df['catalog_number']


        export_to_csv(df, 'output')
    else:
        print('Error')

