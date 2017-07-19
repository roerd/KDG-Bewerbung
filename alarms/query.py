from datetime import timedelta


def get_alarms_for_element(df, element_id):
    return df[df['ELEMENT ID'] == element_id]


def get_alarms_in_interval(df, start_time, end_time):
    return df[(start_time <= df['START']) & (df['START'] <= end_time)
              | (start_time <= df['end']) & (df['end'] <= end_time)]


def sum_alarm_durations(df):
    return sum((row['end'] - row['START'] for _, row in df.iterrows()), timedelta())
