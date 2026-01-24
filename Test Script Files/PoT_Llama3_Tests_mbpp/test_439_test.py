import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_edge_case_empty_list(self):
        self.assertEqual(multiple_to_single([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(multiple_to_single([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_edge_case_mixed_signs(self):
        self.assertEqual(multiple_to_single([1, -2, 3]), 13)

    def test_edge_case_large_numbers(self):
        self.assertEqual(multiple_to_single([9, 9, 9, 9, 9, 9, 9, 9, 9, 9]), 9999999999)

    def test_edge_case_large_negative_numbers(self):
        self.assertEqual(multiple_to_single([-9, -9, -9, -9, -9, -9, -9, -9, -9, -9]), -9999999999)

    def test_edge_case_mixed_types(self):
        with self.assertRaises(TypeError):
            multiple_to_single([1, "2", 3])

    def test_edge_case_non_integer_types(self):
        with self.assertRaises(TypeError):
            multiple_to_single([1, 2.5, 3])
