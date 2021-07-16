#!/usr/bin/env python3

import pandas as pd
import sys

def create_df(file):
    df = pd.read_excel(file, skiprows=4)
    return df

def transform(df):
    df['Unnamed: 0'] = df['Unnamed: 0'].fillna(method='ffill').str.lstrip()
    df.dropna(subset=['Date'], inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Memo/Description'] = df['Memo/Description'].str.split('  ').str[0]
    return df

def export_to_csv(df, root):
    df.to_csv(f'{root}.csv', index=False)

def transform_catalog(df):
    df['Customer'] = df['Customer'].str.replace('Record Production:','').str[0:6]
    df.rename(columns={'Date': 'date',
                    'Customer': 'catalog_number',
                    'Name': 'vendor',
                    'Memo/Description': 'description',
                    'Class': 'expense_type',
                    'Amount': 'net'},
                   inplace=True)
    return df

def transform_artist(df):
    df.rename(columns={
        'Date': 'date',
        'Customer': 'artist_name',
        'Name': 'vendor',
        'Memo/Description': 'description',
        'Class': 'expense_type',
        'Amount': 'net'},
       inplace=True)
    df['artist_name'] = df['artist_name'].str.split('Artists:').str[1]
    df['item_type'] = 'Payout'
    return df

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '-a':
            print(sys.argv[1])
            print('artist')
            file = sys.argv[2]
            root = file.split('.')[0]
            df = create_df(file)
            df = transform(df)
            df = transform_artist(df)
        if sys.argv[1] == '-c':
            print('catalog')
            file = sys.argv[2]
            root = file.split('.')[0]
            df = create_df(file)
            df = transform(df)
            df = transform_catalog(df)
        # else:
        #     file = sys.argv[1]
    else:
        print("Incorrect format")

    export_to_csv(df, root)

