import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_simple_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 3, 4)))
        self.assertTrue(check_smaller((3, 2, 1), (2, 3, 4)))
        self.assertTrue(check_smaller((1, 1, 1), (2, 2, 2)))

    def test_edge_cases(self):
        self.assertFalse(check_smaller((1, 2, 3), (3, 2, 1)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 3, 2)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 3)))
        self.assertFalse(check_smaller((1, 2, 3), ()))
        self.assertFalse(check_smaller((), (1, 2, 3)))

    def test_complex_cases(self):
        self.assertTrue(check_smaller((0, 1, 2), (1, 2, 3)))
        self.assertTrue(check_smaller((-1, 0, 1), (0, 1, 2)))
        self.assertFalse(check_smaller((1, 2, 3), (-1, 0, 1)))
        self.assertFalse(check_smaller((1, 2, 3), (1, 0, -1)))
