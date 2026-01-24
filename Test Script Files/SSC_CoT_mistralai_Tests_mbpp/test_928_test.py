import unittest
from mbpp_928_code import datetime, timedelta
from dateutil.relativedelta import relativedelta
from 928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-12-01'), '01-12-2022')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(change_date_format('2022'), '2022-01-01')
        self.assertEqual(change_date_format('2022-12-31 12:34:56'), '31-12-2022 12:34:56')
        self.assertEqual(change_date_format('2022-01-01T12:34:56'), '01-01-2022 12:34:56')
        self.assertEqual(change_date_format('2022-12-31T23:59:59'), '31-12-2022 23:59:59')
        self.assertEqual(change_date_format('2022-02-29'), '29-02-2022')
        self.assertEqual(change_date_format('2022-12-30'), '30-12-2022')
        self.assertEqual(change_date_format('2022-12-310'), '31-12-2022')
        self.assertEqual(change_date_format('2022-12-31-0'), '31-12-2022')
        self.assertEqual(change_date_format('2022-12-31Z'), '31-12-2022')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, change_date_format, 'abc')
        self.assertRaises(ValueError, change_date_format, '2022-13-31')
        self.assertRaises(ValueError, change_date_format, '2022-02-32')

    def test_datetime_objects(self):
        dt = datetime(2022, 12, 31)
        self.assertEqual(change_date_format(dt), '31-12-2022')
        dt += timedelta(days=1)
        self.assertEqual(change_date_format(dt), '01-12-2022')
        dt += relativedelta(years=1)
        self.assertEqual(change_date_format(dt), '31-12-2023')
