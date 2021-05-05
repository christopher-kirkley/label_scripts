#!/usr/bin/env python3

import pandas as pd
import sys

file = sys.argv[1]
root = file.split('.')[0]

def create_df(file):
    df = pd.read_excel(file, skiprows=4)
    return df

def transform(df):
    df['Unnamed: 0'] = df['Unnamed: 0'].fillna(method='ffill').str.lstrip()
    df.dropna(subset=['Date'], inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Memo/Description'] = df['Memo/Description'].str.split('  ').str[0]
    return df

def export_to_csv(df):
    df.to_csv(f'{root}.csv', index=False)

df = create_df(file)
df = transform(df)
export_to_csv(df)

