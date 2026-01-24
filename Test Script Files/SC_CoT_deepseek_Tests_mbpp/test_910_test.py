import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_date(1, 1, 2022))

    def test_edge_cases(self):
        self.assertTrue(check_date(1, 1, 1))
        self.assertTrue(check_date(12, 31, 9999))
        self.assertFalse(check_date(13, 1, 2022))
        self.assertFalse(check_date(1, 0, 2022))
        self.assertFalse(check_date(1, 32, 2022))

    def test_corner_cases(self):
        self.assertTrue(check_date(1, 1, 1000))
        self.assertFalse(check_date(1, 1, 9999))
        self.assertFalse(check_date(1, 1, 0))

    def test_invalid_inputs(self):
        self.assertFalse(check_date('a', 1, 2022))
        self.assertFalse(check_date(1, 'a', 2022))
        self.assertFalse(check_date(1, 1, 'a'))
        self.assertFalse(check_date(1, 1, 2022))
