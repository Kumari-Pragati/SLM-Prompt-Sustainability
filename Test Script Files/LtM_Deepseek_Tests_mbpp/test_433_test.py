import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_empty_array(self):
        self.assertEqual(check_greater([], 1), 'No, entered number is less than those in the array')

    def test_edge_case_max_value(self):
        self.assertEqual(check_greater([1000000000], 1000000001), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_min_value(self):
        self.assertEqual(check_greater([-1000000000], -999999999), 'No, entered number is less than those in the array')

    def test_complex_case_same_number(self):
        self.assertEqual(check_greater([5, 5, 5], 5), 'Yes, the entered number is greater than those in the array')

    def test_complex_case_number_in_array(self):
        self.assertEqual(check_greater([1, 2, 3], 2), 'Yes, the entered number is greater than those in the array')

    def test_complex_case_number_less_than_all(self):
        self.assertEqual(check_greater([1, 2, 3], 0), 'No, entered number is less than those in the array')
