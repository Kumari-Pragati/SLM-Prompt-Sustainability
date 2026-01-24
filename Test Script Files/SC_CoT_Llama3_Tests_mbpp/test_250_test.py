import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 3), 1)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_X((), 1), 0)

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(count_X((1,), 1), 1)

    def test_edge_case_tuple_with_single_element(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 5), 1)

    def test_edge_case_tuple_with_multiple_elements(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 2), 1)

    def test_edge_case_tuple_with_no_match(self):
        self.assertEqual(count_X((1, 2, 3, 4, 5), 6), 0)

    def test_edge_case_tuple_with_duplicates(self):
        self.assertEqual(count_X((1, 2, 2, 3, 4, 4, 5), 4), 2)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            count_X(123, 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            count_X((1, 2, 3), 'a')
