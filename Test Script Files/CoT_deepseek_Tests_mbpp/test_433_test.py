import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 8), 
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_greater_than_max(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 10), 
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_less_than_min(self):
        self.assertEqual(check_greater([5, 1, 9, 3, 7], 0), 
                         'No, entered number is less than those in the array')

    def test_edge_case_single_element(self):
        self.assertEqual(check_greater([5], 5), 
                         'Yes, the entered number is greater than those in the array')

    def test_edge_case_single_element_less(self):
        self.assertEqual(check_greater([5], 6), 
                         'No, entered number is less than those in the array')

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            check_greater(123, 5)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            check_greater(['a', 'b', 'c'], 'd')
