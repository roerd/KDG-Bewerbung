def get_alarms_for_element(df, element_id):
    return df[df['ELEMENT ID'] == element_id]


def get_alarms_in_interval(df, start_time, end_time):
    return df[start_time <= df['START'] <= end_time or start_time <= df['end'] <= end_time]