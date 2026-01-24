import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_date(1, 1, 2000))

    def test_edge_case(self):
        self.assertTrue(check_date(1, 1, 1))
        self.assertTrue(check_date(12, 31, 9999))

    def test_boundary_case(self):
        self.assertTrue(check_date(1, 1, 2000))
        self.assertTrue(check_date(12, 31, 2000))
        self.assertFalse(check_date(0, 1, 2000))
        self.assertFalse(check_date(13, 1, 2000))
        self.assertFalse(check_date(1, 0, 2000))
        self.assertFalse(check_date(1, 32, 2000))
        self.assertFalse(check_date(1, 1, 0))
        self.assertFalse(check_date(1, 1, 10000))

    def test_invalid_input(self):
        self.assertFalse(check_date('a', 1, 2000))
        self.assertFalse(check_date(1, 'a', 2000))
        self.assertFalse(check_date(1, 1, 'a'))
        self.assertFalse(check_date(1, 1, 2000.5))
        self.assertFalse(check_date(1.5, 1, 2000))
        self.assertFalse(check_date(1, 1.5, 2000))
        self.assertFalse(check_date(1, 1, 2000))
