import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_X((1, 2, 'X', 4, 'X'), 'X'), 2)

    def test_edge_case_empty_tuple(self):
        self.assertEqual(count_X((), 'X'), 0)

    def test_boundary_case_single_element_tuple(self):
        self.assertEqual(count_X(('X',), 'X'), 1)
        self.assertEqual(count_X(('X',), 'Y'), 0)

    def test_boundary_case_tuple_with_non_string_elements(self):
        self.assertEqual(count_X((1, 2, 'X', 4, 'X'), 1), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_X(123, 'X')
