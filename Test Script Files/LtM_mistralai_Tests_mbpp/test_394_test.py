import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_simple_distinct(self):
        self.assertTrue(check_distinct((1, 2, 3)))
        self.assertTrue(check_distinct((3, 4, 5)))
        self.assertTrue(check_distinct((6, 7, 8)))

    def test_simple_not_distinct(self):
        self.assertFalse(check_distinct((1, 1, 2)))
        self.assertFalse(check_distinct((2, 2, 3)))
        self.assertFalse(check_distinct((3, 3, 4)))

    def test_edge_cases(self):
        self.assertTrue(check_distinct(()))
        self.assertTrue(check_distinct((1,)))
        self.assertTrue(check_distinct((1, 2)))

    def test_boundary_cases(self):
        self.assertTrue(check_distinct((-1, 0, 1)))
        self.assertTrue(check_distinct((0, 0, 1)))
        self.assertTrue(check_distinct((1, 2, 255)))
