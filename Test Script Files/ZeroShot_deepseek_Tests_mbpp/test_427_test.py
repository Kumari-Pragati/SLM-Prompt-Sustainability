import unittest
from mbpp_427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_valid_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2022-12-31'), '31-12-2022')
        self.assertEqual(change_date_format('2000-02-29'), '29-02-2000')

    def test_invalid_date(self):
        self.assertEqual(change_date_format('2022-13-01'), '2022-13-01')
        self.assertEqual(change_date_format('2022-01-32'), '2022-01-32')
        self.assertEqual(change_date_format('2022-12-32'), '2022-12-32')
        self.assertEqual(change_date_format('2022-13-32'), '2022-13-32')

    def test_invalid_format(self):
        self.assertEqual(change_date_format('2022/01/01'), '2022/01/01')
        self.assertEqual(change_date_format('2022.01.01'), '2022.01.01')
        self.assertEqual(change_date_format('20220101'), '20220101')
