import datetime
import unittest

import pytz

from UnicornTicketSystem.helpers import datetime_range


class TestDateRangeMethods(unittest.TestCase):
    tz = pytz.timezone("Europe/London")

    def test_second(self):
        date = self.tz.localize(
            datetime.datetime(
                year=2019,
                month=7,
                day=17,
                hour=12,
                minute=25,
                second=45,
                microsecond=0
            )
        )

        lower_date = date.replace(microsecond=0)
        upper_date = date.replace(microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'second'),
            (
                lower_date,
                upper_date
            )
        )

    def test_minute(self):
        date = self.tz.localize(
            datetime.datetime(
                year=2019,
                month=7,
                day=17,
                hour=12,
                minute=25,
                second=45,
                microsecond=0
            )
        )

        lower_date = date.replace(second=0, microsecond=0)
        upper_date = date.replace(second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'minute'),
            (
                lower_date,
                upper_date
            )
        )

    def test_hour(self):
        date = self.tz.localize(
            datetime.datetime(
                year=2019,
                month=7,
                day=17,
                hour=12,
                minute=25,
                second=45,
                microsecond=0
            )
        )

        lower_date = date.replace(minute=0, second=0, microsecond=0)
        upper_date = date.replace(minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'hour'),
            (
                lower_date,
                upper_date
            )
        )

    def test_day(self):
        date = self.tz.localize(
            datetime.datetime(
                year=2019,
                month=7,
                day=17,
                hour=12,
                minute=25,
                second=45,
                microsecond=0
            )
        )

        lower_date = date.replace(hour=0, minute=0, second=0, microsecond=0)
        upper_date = date.replace(hour=23, minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'day'),
            (
                lower_date,
                upper_date
            )
        )

    def test_month(self):
        date = self.tz.localize(
            datetime.datetime(
                year=2019,
                month=7,
                day=17,
                hour=12,
                minute=25,
                second=45,
                microsecond=0
            )
        )

        lower_date = date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        upper_date = date.replace(day=31, hour=23, minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'month'),
            (
                lower_date,
                upper_date
            )
        )

    def test_year(self):
        date = datetime.datetime(
            year=2019,
            month=7,
            day=17,
            hour=12,
            minute=25,
            second=45,
            microsecond=0
        )

        lower_date = date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        upper_date = date.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'year'),
            (
                self.tz.localize(lower_date),
                self.tz.localize(upper_date),
            )
        )

    def test_month_february(self):
        date = datetime.datetime(
            year=2019,
            month=2,
            day=17,
            hour=12,
            minute=25,
            second=45,
            microsecond=0
        )

        lower_date = date.replace(month=2, day=1, hour=0, minute=0, second=0, microsecond=0)
        upper_date = date.replace(month=2, day=28, hour=23, minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'month'),
            (
                self.tz.localize(lower_date),
                self.tz.localize(upper_date)
            )
        )

    def test_year_from_february(self):
        date = datetime.datetime(
            year=2019,
            month=2,
            day=17,
            hour=12,
            minute=25,
            second=45,
            microsecond=0
        )

        lower_date = date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        upper_date = date.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'year'),
            (
                self.tz.localize(lower_date),
                self.tz.localize(upper_date)
            )
        )

    def test_week(self):
        date = self.tz.localize(
            datetime.datetime(
                year=2019,
                month=7,
                day=17,
                hour=12,
                minute=25,
                second=45,
                microsecond=0
            )
        )

        lower_date = date.replace(day=15, hour=0, minute=0, second=0, microsecond=0)
        upper_date = date.replace(day=21, hour=23, minute=59, second=59, microsecond=999999)

        self.assertEqual(
            datetime_range(date, 'week'),
            (
                lower_date,
                upper_date
            )
        )
