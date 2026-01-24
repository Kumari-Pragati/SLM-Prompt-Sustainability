import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_none((1, None, 2)))

    def test_edge_case(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_boundary_case(self):
        self.assertTrue(check_none((None,)))
        self.assertFalse(check_none(()))

    def test_corner_case(self):
        self.assertTrue(check_none((None, None, None)))
        self.assertFalse(check_none((1, 2, 3, 4)))
