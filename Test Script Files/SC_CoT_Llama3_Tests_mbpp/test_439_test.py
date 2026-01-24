import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(multiple_to_single([5]), 5)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(multiple_to_single([-1, 2, -3]), -123)

    def test_edge_case_large_numbers(self):
        self.assertEqual(multiple_to_single([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]), 9999999999)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            multiple_to_single(['a', 'b', 'c'])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            multiple_to_single('abc')
