import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(check_greater([1, 2, 3, 4], 5), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([10, 20, 30, 40], 50), 'Yes, the entered number is greater than those in the array')

    def test_zero_and_negative_numbers(self):
        self.assertEqual(check_greater([-1, -2, -3], 0), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-1, -2, -3], -4), 'No, entered number is less than those in the array')

    def test_empty_list(self):
        self.assertEqual(check_greater([], 1), 'No, entered number is less than those in the array')

    def test_single_element_list(self):
        self.assertEqual(check_greater([1], 1), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-1], -1), 'Yes, the entered number is greater than those in the array')

    def test_duplicate_elements(self):
        self.assertEqual(check_greater([1, 1, 2, 3], 2), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([-1, -1, -2, -3], -2), 'Yes, the entered number is greater than those in the array')

    def test_sorting_behavior(self):
        self.assertEqual(check_greater([3, 2, 1], 4), 'No, entered number is less than those in the array')
        self.assertEqual(check_greater([-3, -2, -1], -4), 'Yes, the entered number is greater than those in the array')
