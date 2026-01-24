import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 8), 
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_greater_than_max(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 10), 
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_equal_to_max(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 9), 
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_less_than_min(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 0), 
                         'No, entered number is less than those in the array')

    def test_edge_case_equal_to_min(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 1), 
                         'No, entered number is less than those in the array')

    def test_typical_case_less_than_all(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 2), 
                         'No, entered number is less than those in the array')

    def test_typical_case_greater_than_all(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 15), 
                         'Yes, the entered number is greater than those in the array')

    def test_empty_array(self):
        self.assertEqual(check_greater([], 5), 
                         'Yes, the entered number is greater than those in the array')

    def test_single_element_array(self):
        self.assertEqual(check_greater([5], 10), 
                         'Yes, the entered number is greater than those in the array')

    def test_single_element_array_equal(self):
        self.assertEqual(check_greater([5], 5), 
                         'Yes, the entered number is greater than those in the array')

    def test_single_element_array_less(self):
        self.assertEqual(check_greater([5], 0), 
                         'No, entered number is less than those in the array')
