import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_equal(self):
        self.assertEqual(check_greater([1, 2, 3], 3), 'No, entered number is less than those in the array')

    def test_edge_case_smaller(self):
        self.assertEqual(check_greater([1, 2, 3], 0), 'No, entered number is less than those in the array')

    def test_edge_case_larger(self):
        self.assertEqual(check_greater([1, 2, 3], 10), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_single_element(self):
        self.assertEqual(check_greater([5], 5), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_empty_array(self):
        with self.assertRaises(IndexError):
            check_greater([], 5)

    def test_edge_case_single_element_equal(self):
        self.assertEqual(check_greater([5], 5), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_single_element_smaller(self):
        self.assertEqual(check_greater([5], 0), 'No, entered number is less than those in the array')

    def test_edge_case_single_element_larger(self):
        self.assertEqual(check_greater([5], 10), 'Yes, the entered number is greater than those in the array')
