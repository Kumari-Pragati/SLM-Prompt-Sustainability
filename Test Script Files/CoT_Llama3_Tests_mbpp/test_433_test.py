import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_equal(self):
        self.assertEqual(check_greater([1, 2, 3], 3), 'No, entered number is less than those in the array')

    def test_edge_case_smaller(self):
        self.assertEqual(check_greater([1, 2, 3], 0), 'No, entered number is less than those in the array')

    def test_edge_case_empty_array(self):
        self.assertEqual(check_greater([], 5), 'No, entered number is less than those in the array')

    def test_edge_case_single_element_array(self):
        self.assertEqual(check_greater([5], 4), 'No, entered number is less than those in the array')

    def test_edge_case_single_element_array_equal(self):
        self.assertEqual(check_greater([5], 5), 'No, entered number is less than those in the array')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_greater('abc', 5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            check_greater([1, 2, 3], 'abc')
