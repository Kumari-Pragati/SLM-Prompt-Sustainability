import unittest
from mbpp_132_code import tup_string

class TestTupString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(tup_string(('a', 'b', 'c')), 'abc')

    def test_edge_case_empty_tuple(self):
        self.assertEqual(tup_string(()), '')

    def test_edge_case_single_element_tuple(self):
        self.assertEqual(tup_string(('x',)), 'x')

    def test_boundary_case_single_character_tuple(self):
        self.assertEqual(tup_string(('A',)), 'A')

    def test_boundary_case_single_digit_tuple(self):
        self.assertEqual(tup_string((1,)), '1')

    def test_corner_case_mixed_types(self):
        self.assertRaises(TypeError, tup_string, (1, 'a'))
