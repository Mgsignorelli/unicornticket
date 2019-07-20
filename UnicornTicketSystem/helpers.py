import calendar
from datetime import timedelta

import pytz


def datetime_range(date, time_range):
    print('date: ' + str(date))
    print('time_range: ' + str(time_range))
    tz = pytz.timezone('Europe/London')
    if date.tzinfo:
        date = date.replace(tzinfo=None)

    time_ranges = ['', 'second', 'minute', 'hour', 'day', 'week', 'month', 'year']
    time_range_index = time_ranges.index(time_range)

    lower = {}
    upper = {}

    if time_range_index > 6:
        lower['month'] = 1
        upper['month'] = 12

    if time_range_index > 5:
        lower['day'] = 1
        month = upper.get('month') if upper.get('month') is not None else date.month
        upper['day'] = calendar.monthrange(date.year, month)[1]

    if time_range_index == 5:
        lower_date = date - timedelta(days=date.weekday())
        lower['day'] = lower_date.day
        upper['day'] = (lower_date + timedelta(days=6)).day

    if time_range_index > 3:
        lower['hour'] = 0
        upper['hour'] = 23

    if time_range_index > 2:
        lower['minute'] = 0
        upper['minute'] = 59

    if time_range_index > 1:
        lower['second'] = 0
        upper['second'] = 59

    if time_range_index > 0:
        lower['microsecond'] = 0
        upper['microsecond'] = 999999

    return tz.localize(date.replace(**lower)), tz.localize(date.replace(**upper))
