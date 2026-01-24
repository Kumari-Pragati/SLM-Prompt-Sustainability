import unittest
from mbpp_433_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(check_greater([1, 2, 3], 4), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_lower(self):
        self.assertEqual(check_greater([1, 2, 3], 1), 'No, entered number is less than those in the array')

    def test_edge_case_higher(self):
        self.assertEqual(check_greater([1, 2, 3], 5), 'Yes, the entered number is greater than those in the array')

    def test_edge_case_equal(self):
        self.assertEqual(check_greater([1, 2, 3], 2), 'No, entered number is less than those in the array')

    def test_empty_array(self):
        self.assertEqual(check_greater([], 1), 'No, entered number is less than those in the array')

    def test_single_element_array(self):
        self.assertEqual(check_greater([1], 1), 'Yes, the entered number is greater than those in the array')

    def test_single_element_array_lower(self):
        self.assertEqual(check_greater([1], 0), 'No, entered number is less than those in the array')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_greater('array', 1)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            check_greater([1, 2, 3], 'number')
