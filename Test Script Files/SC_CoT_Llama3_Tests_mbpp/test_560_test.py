import unittest
from mbpp_560_code import union_elements

class TestUnionElements(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(union_elements((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_edge_case_empty_input(self):
        self.assertEqual(union_elements((), ()), ())

    def test_edge_case_single_input(self):
        self.assertEqual(union_elements((1, 2, 3), ()), (1, 2, 3))

    def test_edge_case_single_input_empty(self):
        self.assertEqual(union_elements((), (1, 2, 3)), (1, 2, 3))

    def test_edge_case_duplicates(self):
        self.assertEqual(union_elements((1, 2, 2), (2, 3, 4)), (1, 2, 3, 4))

    def test_edge_case_duplicates_reverse(self):
        self.assertEqual(union_elements((2, 2, 3), (1, 2, 4)), (1, 2, 3, 4))

    def test_edge_case_duplicates_reverse_empty(self):
        self.assertEqual(union_elements((), (2, 2, 3), (1, 2, 4)), (1, 2, 3, 4))

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            union_elements(123, (1, 2, 3))

    def test_invalid_input_non_tuple_reverse(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), 123)

    def test_invalid_input_non_tuple_empty(self):
        with self.assertRaises(TypeError):
            union_elements(123, ())

    def test_invalid_input_non_tuple_empty_reverse(self):
        with self.assertRaises(TypeError):
            union_elements((1, 2, 3), 123)
