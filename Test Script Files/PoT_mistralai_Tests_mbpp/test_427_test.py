import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')
        self.assertEqual(change_date_format('2021-02-28'), '28-02-2021')
        self.assertEqual(change_date_format('2000-01-01'), '01-01-2000')

    def test_edge_cases(self):
        self.assertEqual(change_date_format('2022-12-30'), '30-12-2022')
        self.assertEqual(change_date_format('2022-12-01'), '01-12-2022')
        self.assertEqual(change_date_format('2022-02-29'), '29-02-2022')
        self.assertEqual(change_date_format('2022-02-31'), '31-02-2022')  # Leap year edge case
        self.assertEqual(change_date_format('2022-13-31'), None)  # Invalid month
        self.assertEqual(change_date_format('2022-00-01'), None)  # Invalid day
        self.assertEqual(change_date_format('-12-31'), None)  # Invalid year
        self.assertEqual(change_date_format('2022-12-31T12:34:56'), None)  # Invalid format
