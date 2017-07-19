import pandas as pd
from datetime import datetime
from pathlib import Path


def add_date(date):
    """
    Hilfsfunktion zum Einlesen der Spalten 2 und 3 der Diagnose-Logs.
    :param date: datetime-Objekt, das den Tag des Logs repräsentiert
    :return: datetime mit Datums- und Zeitangabe
    """
    def add_time(time_str):
        time = datetime.strptime(time_str, '%H:%M:%S').time()
        return datetime.combine(date, time)
    return add_time


def read_csv(path):
    """
    Liest ein Diagnose-Logdatei im CSV-Format ein.
    
    :param path: Dateiname des Logs, z.B. "ALARMS_20110102.csv" 
    :return: pandas-Dataframe mit den vier Spalten Element-ID, Start, Ende, Severity
    """
    base = Path(path).name

    date = datetime.strptime(base, 'alarms_%Y%m%d.csv')

    df = pd.read_csv(path, parse_dates=[1, 2], date_parser=add_date(date))

    return df


def read_dir(path):
    """
    Liest alle Diagnose-Logdateien in einem Verzeichnis ein.
    :param path: Verzeichnisname, z.B. "." oder "C:\Logs\2016"
    :return: pandas-Dataframe mit den vier Spalten Element-ID, Start, Ende, Severity
    """
    p = Path(path)

    df = None

    for file in p.glob('alarms_*.csv'):
        file_df = read_csv(file)

        if df is None:
            df = file_df
        else:
            df = df.append(file_df, ignore_index=True)

    return df
