import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_simple_increasing_array(self):
        self.assertTrue(check([1, 2, 3, 4], 4))

    def test_simple_decreasing_array(self):
        self.assertTrue(check([4, 3, 2, 1], 4))

    def test_simple_constant_array(self):
        self.assertTrue(check([1, 1, 1, 1], 4))

    def test_edge_empty_array(self):
        self.assertFalse(check([], 0))

    def test_edge_single_element_array(self):
        self.assertTrue(check([1], 1))

    def test_edge_two_elements_array(self):
        self.assertTrue(check([1, 1], 2))

    def test_edge_negative_array(self):
        self.assertFalse(check([-1, -2, -3], 3))

    def test_edge_zero_array(self):
        self.assertTrue(check([0], 1))
        self.assertTrue(check([0, 0], 2))

    def test_complex_alternating_array(self):
        self.assertFalse(check([1, -1, 1, -1], 4))

    def test_complex_increasing_then_decreasing_array(self):
        self.assertFalse(check([1, 2, 3, 2, 1], 5))

    def test_complex_decreasing_then_increasing_array(self):
        self.assertFalse(check([4, 3, 2, 3, 4], 5))
