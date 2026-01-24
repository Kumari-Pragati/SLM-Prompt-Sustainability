import unittest
from mbpp_427_code import datetime
from 427_code import change_date_format

class TestChangeDateFormat(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(change_date_format(''), '')

    def test_invalid_date_format(self):
        self.assertRaises(ValueError, change_date_format, 'invalid_date')

    def test_date_format(self):
        for test_date in [
                '2022-12-31',
                '2022-12-31T23:59:59',
                '2022-12-31 23:59:59',
                '2022-12-31 23:59:59.999999',
                '2022-12-31 23:59:59Z',
                '2022-12-31 23:59:59+00:00',
                '2022-12-31 23:59:59-05:00',
                datetime.now().strftime('%Y-%m-%d')
        ]:
            self.assertEqual(change_date_format(test_date), test_date)
