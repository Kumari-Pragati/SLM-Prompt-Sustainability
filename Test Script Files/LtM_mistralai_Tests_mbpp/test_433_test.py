import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_simple_greater(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_simple_less(self):
        self.assertEqual(check_greater([1, 2, 3], 1), 'No, entered number is less than those in the array')

    def test_empty_list(self):
        self.assertEqual(check_greater([], 2), 'No, entered number is less than those in the array')

    def test_single_element_list(self):
        self.assertEqual(check_greater([1], 2), 'Yes, the entered number is greater than those in the array')

    def test_sorted_list(self):
        self.assertEqual(check_greater([1, 2, 3], 3), 'Yes, the entered number is greater than those in the array')

    def test_reverse_sorted_list(self):
        self.assertEqual(check_greater([3, 2, 1], 4), 'Yes, the entered number is greater than those in the array')

    def test_negative_numbers(self):
        self.assertEqual(check_greater([-1, -2, -3], -4), 'Yes, the entered number is greater than those in the array')

    def test_zero(self):
        self.assertEqual(check_greater([-1, 0, 1], 0), 'No, entered number is less than those in the array')
