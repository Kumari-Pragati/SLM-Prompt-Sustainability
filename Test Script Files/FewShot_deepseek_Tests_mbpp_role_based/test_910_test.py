import unittest
from mbpp_910_code import check_date

class TestCheckDate(unittest.TestCase):
    def test_typical_date(self):
        self.assertTrue(check_date(1, 1, 2000))

    def test_boundary_dates(self):
        self.assertTrue(check_date(1, 1, 1))
        self.assertTrue(check_date(12, 31, 9999))

    def test_edge_dates(self):
        self.assertFalse(check_date(0, 1, 2000))
        self.assertFalse(check_date(13, 1, 2000))
        self.assertFalse(check_date(1, 0, 2000))
        self.assertFalse(check_date(1, 32, 2000))

    def test_invalid_inputs(self):
        self.assertFalse(check_date('a', 1, 2000))
        self.assertFalse(check_date(1, 'b', 2000))
        self.assertFalse(check_date(1, 1, 'c'))
        self.assertFalse(check_date(1, 1, 200000))
