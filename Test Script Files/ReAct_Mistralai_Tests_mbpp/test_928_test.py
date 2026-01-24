import unittest
from mbpp_928_code import datetime, date, timedelta
from 928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_valid_date_format(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-01-31'), '31-01-2022')
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_invalid_date_format(self):
        self.assertRaises(ValueError, change_date_format, 'invalid_date')
        self.assertRaises(ValueError, change_date_format, '2022-32-01')
        self.assertRaises(ValueError, change_date_format, '2022-01-00')

    def test_date_object(self):
        dt = datetime(2022, 1, 1)
        self.assertEqual(change_date_format(dt.strftime('%Y-%m-%d')), '01-01-2022')

        dt = datetime(2022, 2, 29)  # Leap year for demonstration
        self.assertEqual(change_date_format(dt.strftime('%Y-%m-%d')), '29-02-2022')

    def test_date_object_with_time(self):
        dt = datetime(2022, 1, 1, 12, 30, 45)
        self.assertEqual(change_date_format(dt.strftime('%Y-%m-%d %H:%M:%S')), '01-01-2022')

    def test_date_object_with_time_and_timezone(self):
        dt = datetime(2022, 1, 1, 12, 30, 45, tzinfo=datetime.timezone.utc)
        self.assertEqual(change_date_format(dt.astimezone(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')), '01-01-2022')

    def test_date_object_with_time_and_timezone_invalid_format(self):
        dt = datetime(2022, 1, 1, 12, 30, 45, tzinfo=datetime.timezone.utc)
        self.assertRaises(ValueError, change_date_format, dt.astimezone(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S%z'))
