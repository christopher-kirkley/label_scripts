import numpy as np
import pandas as pd
import pyperclip
import sys
import os
from datetime import datetime
from pandas.io.clipboard import copy

SCRIPTDIR="~/work_scripts/release_dates_script/"

def main():
    release_date = input('Choose a release date DD/MM/YY: ')

    df = pd.read_csv(f'{SCRIPTDIR}release_dates.csv', index_col='Release Date')

    try:
        dates_df = df.loc[release_date]
        dates = dates_df.to_dict()

        return dates

    except KeyError:
        print('Invalid date')

    return dates

def output_string(dates):
    output = ""

    for key, value in dates.items():
        output = output + f"{key}: {value}\n"
    
    pyperclip.copy(output)
    return output

# check that is not empty

def write_to_emacs(dates, filename):
    with open(filename, 'a') as f:
        f.write('\n* TIMELINE\n')
        for item, date in dates.items():
            try:
                date_object = datetime.strptime(date, '%m/%d/%y')
                date = date_object.strftime('%Y-%m-%d %a')

                f.write(f'** TODO {item}\n')
                f.write(f'  DEADLINE: <{date}>\n')
            except:
                pass
        
if __name__ == "__main__":
    dates = main()
    if len(sys.argv) > 1:
        if sys.argv[1] == '-e':
            write_to_emacs(dates, sys.argv[2])
        else:
            pass
    else:
        copy(output_string(dates))
        
        

