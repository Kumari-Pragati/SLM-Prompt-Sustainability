import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_simple_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')

    def test_edge_dates(self):
        self.assertEqual(change_date_format('2000-01-01'), '01-01-2000')
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')

    def test_boundary_dates(self):
        self.assertEqual(change_date_format('2022-02-28'), '28-02-2022')
        self.assertEqual(change_date_format('2022-02-29'), '29-02-2022')  # Leap year

    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            change_date_format('2022-13-01')
        with self.assertRaises(ValueError):
            change_date_format('2022-02-30')

    def test_special_dates(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-06-30'), '30-06-2022')
