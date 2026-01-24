import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_simple_none(self):
        self.assertTrue(check_none((None,)))
        self.assertTrue(check_none((None, 1)))
        self.assertTrue(check_none((1, None)))

    def test_simple_not_none(self):
        self.assertFalse(check_none((1, 1)))

    def test_edge_cases(self):
        self.assertTrue(check_none(()))
        self.assertTrue(check_none((None, None)))
        self.assertFalse(check_none((1,)))
