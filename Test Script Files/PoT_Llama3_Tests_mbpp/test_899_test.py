import unittest
from mbpp_899_code import check

class TestCheck(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_edge_case_non_decreasing(self):
        self.assertTrue(check([1, 1, 1, 1, 1], 5))

    def test_edge_case_non_increasing(self):
        self.assertTrue(check([5, 4, 3, 2, 1], 5))

    def test_edge_case_equal(self):
        self.assertTrue(check([1, 1, 1, 1, 1], 5))

    def test_edge_case_single_element(self):
        self.assertTrue(check([1], 1))

    def test_edge_case_empty(self):
        with self.assertRaises(TypeError):
            check([], 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            check([-1], -1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            check([1.0, 2.0, 3.0], 3)

    def test_edge_case_non_positive(self):
        with self.assertRaises(TypeError):
            check([-1, -2, -3], 3)
