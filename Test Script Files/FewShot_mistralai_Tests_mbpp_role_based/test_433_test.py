import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_greater_than_all_elements(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_equal_to_last_element(self):
        self.assertEqual(check_greater([1, 2, 3], 3), 'Yes, the entered number is greater than those in the array')

    def test_less_than_all_elements(self):
        self.assertEqual(check_greater([5, 6, 7], 4), 'No, entered number is less than those in the array')

    def test_empty_list(self):
        self.assertEqual(check_greater([], 5), 'No, entered number is less than those in the array')

    def test_single_element_list(self):
        self.assertEqual(check_greater([5], 6), 'Yes, the entered number is greater than those in the array')

    def test_negative_number(self):
        self.assertEqual(check_greater([-1, -2, -3], -4), 'Yes, the entered number is greater than those in the array')
