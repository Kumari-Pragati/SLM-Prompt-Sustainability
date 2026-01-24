import unittest
from mbpp_899_code import check

class TestCheckFunction(unittest.TestCase):

    def test_positive_sequence(self):
        self.assertTrue(check([1, 2, 3, 4, 5], 5))

    def test_negative_sequence(self):
        self.assertTrue(check([-1, -2, -3, -4, -5], 5))

    def test_mixed_sequence(self):
        self.assertTrue(check([1, -2, 3, -4, 5], 5))

    def test_single_element(self):
        self.assertTrue(check([1], 1))

    def test_empty_list(self):
        self.assertFalse(check([], 0))

    def test_decreasing_sequence_with_single_increase(self):
        self.assertFalse(check([1, 2, 3, 2, 1], 5))

    def test_increasing_sequence_with_single_decrease(self):
        self.assertFalse(check([1, 2, 3, 4, -1], 5))

    def test_invalid_input_list(self):
        self.assertRaises(TypeError, check, 'invalid_input', 1)

    def test_invalid_input_list_length(self):
        self.assertRaises(ValueError, check, [1], 0)
        self.assertRaises(ValueError, check, [1], -1)
