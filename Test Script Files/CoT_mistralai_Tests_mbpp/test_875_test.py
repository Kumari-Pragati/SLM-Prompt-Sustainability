import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_difference([]), 0)

    def test_single_element_list(self):
        self.assertEqual(min_difference([1]), 0)

    def test_two_elements_list(self):
        self.assertEqual(min_difference([1, 2]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(min_difference([3, 5, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_difference([-1, -2, -3]), 1)

    def test_positive_and_negative_numbers(self):
        self.assertEqual(min_difference([1, -2, 3]), 1)

    def test_large_numbers(self):
        self.assertEqual(min_difference([1000000001, 1000000000]), 1)

    def test_zero(self):
        self.assertEqual(min_difference([0, 0]), 0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            min_difference("not a list")
