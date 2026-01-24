import unittest
from mbpp_427_code import datetime, timedelta
from 427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-12-01'), '01-12-2022')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(change_date_format('2022-01-31'), '31-01-2022')
        self.assertEqual(change_date_format('2022-13-01'), '01-13-2022')
        self.assertEqual(change_date_format('2022-00-01'), '01-00-2022')
        self.assertEqual(change_date_format('2022-12-00'), '00-12-2022')
        self.assertEqual(change_date_format('2022-31-12'), '31-12-2022')

    def test_special_or_corner_cases(self):
        self.assertEqual(change_date_format('2022-W52-4'), '04-W52-2022')
        self.assertEqual(change_date_format('2022-02-29'), '29-02-2022')
        self.assertEqual(change_date_format('2022-02-28'), '28-02-2022')
        self.assertEqual(change_date_format('2022-02-27'), '27-02-2022')

    def test_invalid_input(self):
        self.assertRaises(ValueError, change_date_format, 'invalid_date')
        self.assertRaises(ValueError, change_date_format, '2022-32-01')
        self.assertRaises(ValueError, change_date_format, '2022-12-32')
        self.assertRaises(ValueError, change_date_format, '2022-01-00')
        self.assertRaises(ValueError, change_date_format, '2022-13-00')
