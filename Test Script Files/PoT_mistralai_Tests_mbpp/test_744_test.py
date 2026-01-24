import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(check_none((1, 2, None)))
        self.assertTrue(check_none((None, 2, 3)))
        self.assertTrue(check_none((None, None, None)))

    def test_edge_cases(self):
        self.assertFalse(check_none((1, 2, 3)))
        self.assertFalse(check_none((1,)))
        self.assertFalse(check_none([]))
