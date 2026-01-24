import unittest
from mbpp_899_code import check

class TestCheck(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_decreasing_sequence(self):
        self.assertFalse(check([5, 4, 3, 2, 1], 5))

    def test_increasing_sequence(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_same_values(self):
        self.assertTrue(check([1, 1, 1, 1, 1], 5))

    def test_empty_array(self):
        self.assertTrue(check([], 0))

    def test_single_element(self):
        self.assertTrue(check([1], 1))

    def test_negative_numbers(self):
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))

    def test_large_numbers(self):
        self.assertTrue(check([1000000, 2000000, 3000000, 4000000, 5000000], 5))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check("1, 2, 3, 4, 5", 5)
