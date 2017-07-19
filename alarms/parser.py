import pandas as pd
from datetime import datetime
from pathlib import Path


def add_date(date):
    def add_time(time_str):
        time = datetime.strptime(time_str, '%H:%M:%S').time()
        return datetime.combine(date, time)
    return add_time


def read_csv(path):
    base = Path(path).name

    date = datetime.strptime(base, 'alarms_%Y%m%d.csv')

    df = pd.read_csv(path, parse_dates=[1, 2], date_parser=add_date(date))

    return df


def read_dir(path):
    p = Path(path)

    df = None

    for file in p.glob('alarms_*.csv'):
        file_df = read_csv(file)

        if df is None:
            df = file_df
        else:
            df = df.append(file_df, ignore_index=True)

    return df
