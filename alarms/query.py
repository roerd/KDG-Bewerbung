from datetime import timedelta


def get_alarms_for_element(df, element_id):
    """
    Extrahiert alle Alarm-Meldungen eines bestimmten Elements.
    :param df: pandas-Dataframe mit den Spalten Element-ID, start, Ende, Severity
    :param element_id: ID eines Elementes, z.b. 17
    :type element_id: int
    :return: gefilterter Dataframe
    """
    return df[df['ELEMENT ID'] == element_id]


def get_alarms_in_interval(df, start_time, end_time):
    """
    Extrahiert alle Alarm-Meldungen, die in ein Zeitintervall fallen.

    :param df: pandas-Dataframe mit den Spalten Element-ID, start, Ende, Severity
    :param start_time: datetime-Objekt der Anfangszeit 
    :param end_time:   datetime-Objekt der Endzeit
    :return: alle Alarm-Meldungen, die sich ganz oder teilweise mit dem Intervall überschneiden.  
    """
    return df[(start_time <= df['START']) & (df['START'] <= end_time)
              | (start_time <= df['end']) & (df['end'] <= end_time)]


def sum_alarm_durations(df):
    """
    Addiert die Dauer aller genannten Alarm-Meldungen.
    
    :param df: pandas-Dataframe mit den Spalten Element-ID, start, Ende, Severity
    :rtype:  timedelta
    :return  Summe der Dauern aller genannten Alarme. Wenn verschiedene Meldungen einander
     überschneiden, wird die gemeinsame Dauer beider Meldungen nicht subtrahiert, 
      d.h. das Ergebnis kann größer sein als der Gesamtzeitraum.
    """
    return sum((row['end'] - row['START'] for _, row in df.iterrows()), timedelta())
