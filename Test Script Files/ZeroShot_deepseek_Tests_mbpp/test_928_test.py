import unittest
from mbpp_928_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_valid_date(self):
        self.assertEqual(change_date_format('2022-01-01'), '01-01-2022')
        self.assertEqual(change_date_format('2020-12-31'), '31-12-2020')
        self.assertEqual(change_date_format('1999-05-15'), '15-05-1999')

    def test_invalid_date(self):
        self.assertNotEqual(change_date_format('2022-13-01'), '01-13-2022')
        self.assertNotEqual(change_date_format('2020-12-32'), '32-12-2020')
        self.assertNotEqual(change_date_format('1999-05-32'), '32-05-1999')
