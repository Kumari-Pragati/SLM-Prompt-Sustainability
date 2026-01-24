import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_length([]), (0, None))

    def test_single_element_list(self):
        self.assertEqual(min_length([1]), (1, 1))

    def test_list_with_single_min_length(self):
        self.assertEqual(min_length([1, 2, 3]), (1, 1))

    def test_list_with_multiple_min_lengths(self):
        self.assertEqual(min_length([1, 1, 2, 3]), (1, 1))

    def test_list_with_min_length_and_non_min_lengths(self):
        self.assertEqual(min_length([1, 2, 3, 1]), (1, 1))

    def test_list_with_negative_numbers(self):
        self.assertEqual(min_length([-1, 2, -3, 4]), (1, -1))

    def test_list_with_strings(self):
        self.assertEqual(min_length(["apple", "banana", "cherry"]), (5, "apple"))

    def test_list_with_mixed_types(self):
        self.assertRaises(TypeError, min_length, [1, "apple", 3.14])
