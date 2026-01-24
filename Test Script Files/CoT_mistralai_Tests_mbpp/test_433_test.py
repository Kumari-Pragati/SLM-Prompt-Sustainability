import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(check_greater([1, 2, 3, 4], 5), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([5, 4, 3, 2], 1), 'No, entered number is less than those in the array')

    def test_zero_and_negative_numbers(self):
        self.assertEqual(check_greater([0, -1, -2], 1), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-5, -4, -3, -2], -6), 'No, entered number is less than those in the array')

    def test_empty_list(self):
        self.assertEqual(check_greater([], 1), 'No, entered number is less than those in the array')

    def test_single_element_list(self):
        self.assertEqual(check_greater([1], 1), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-1], -1), 'Yes, the entered number is greater than those in the array')

    def test_sorted_list(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-1, -2, -3], -4), 'Yes, the entered number is greater than those in the array')

    def test_duplicate_values(self):
        self.assertEqual(check_greater([1, 1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-1, -1, -2, -3], -4), 'Yes, the entered number is greater than those in the array')

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, check_greater, ['a', 'b', 'c'], 1)
        self.assertRaises(TypeError, check_greater, [1, 2, 3], 'a')
