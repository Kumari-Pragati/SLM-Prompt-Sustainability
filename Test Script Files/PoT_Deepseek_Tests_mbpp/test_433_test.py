import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_greater([5, 1, 9, 3], 7), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_number_greater_than_all(self):
        self.assertEqual(check_greater([5, 1, 9, 3], 10), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_number_equal_to_max(self):
        self.assertEqual(check_greater([5, 1, 9, 3], 9), 'No, entered number is less than those in the array')

    def test_edge_case_single_element_array(self):
        self.assertEqual(check_greater([5], 7), 'Yes, the entered number is greater than those in the array')
        self.assertEqual(check_greater([5], 5), 'No, entered number is less than those in the array')

    def test_edge_case_empty_array(self):
        self.assertEqual(check_greater([], 7), 'Yes, the entered number is greater than those in the array')

    def test_corner_case_negative_numbers(self):
        self.assertEqual(check_greater([-5, -1, -9, -3], -7), 'No, entered number is less than those in the array')

    def test_corner_case_duplicate_numbers(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 9], 9), 'No, entered number is less than those in the array')
