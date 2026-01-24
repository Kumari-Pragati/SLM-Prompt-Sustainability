import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 3)
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 5], 3), 2)
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4, 5], 4), 4)

    def test_empty_arrays(self):
        self.assertEqual(find_platform([], [], 0), 0)
        self.assertEqual(find_platform([], [1], 1), 0)
        self.assertEqual(find_platform([1], [], 1), 1)

    def test_single_element_arrays(self):
        self.assertEqual(find_platform([1], [1], 1), 1)
        self.assertEqual(find_platform([1], [2], 1), 0)
        self.assertEqual(find_platform([2], [1], 1), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_platform([-1, -2, -3], [-2, -3, -4], 3), 3)
        self.assertEqual(find_platform([-1, -2, -3], [-2, -3, -5], 3), 2)

    def test_reverse_order(self):
        self.assertEqual(find_platform([3, 2, 1], [2, 3, 4], 3), 3)
        self.assertEqual(find_platform([3, 2, 1], [2, 3, 5], 3), 2)

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            find_platform([1, 2, 3], [2, 3, 4], 0)
        with self.assertRaises(ValueError):
            find_platform([1, 2, 3], [2, 3, 4], 4)
