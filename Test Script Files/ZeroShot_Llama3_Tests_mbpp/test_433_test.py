import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_check_greater_positive(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_check_greater_negative(self):
        self.assertEqual(check_greater([1, 2, 3], 1), 'No, entered number is less than those in the array')

    def test_check_greater_equal(self):
        self.assertEqual(check_greater([1, 2, 3], 3), 'No, entered number is less than those in the array')

    def test_check_greater_empty_array(self):
        self.assertEqual(check_greater([], 5), 'Yes, the entered number is greater than those in the array')

    def test_check_greater_single_element_array(self):
        self.assertEqual(check_greater([5], 4), 'No, entered number is less than those in the array')

    def test_check_greater_array_with_duplicates(self):
        self.assertEqual(check_greater([1, 2, 2, 3], 4), 'Yes, the entered number is greater than those in the array')
