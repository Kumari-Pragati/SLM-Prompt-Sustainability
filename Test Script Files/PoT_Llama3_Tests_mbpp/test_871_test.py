import unittest
from mbpp_871_code import are_Rotations

class TestAreRotations(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(are_Rotations('abc', 'cab'))

    def test_edge_case_equal_strings(self):
        self.assertTrue(are_Rotations('abc', 'abc'))

    def test_edge_case_reverse_strings(self):
        self.assertTrue(are_Rotations('abc', 'cba'))

    def test_edge_case_same_string(self):
        self.assertTrue(are_Rotations('abc', 'abc'))

    def test_edge_case_empty_string(self):
        self.assertFalse(are_Rotations('', 'abc'))

    def test_edge_case_single_char_string(self):
        self.assertFalse(are_Rotations('a', 'b'))

    def test_edge_case_single_char_string2(self):
        self.assertTrue(are_Rotations('a', 'a'))

    def test_edge_case_invalid_input(self):
        with self.assertRaises(TypeError):
            are_Rotations(123, 'abc')

    def test_edge_case_invalid_input2(self):
        with self.assertRaises(TypeError):
            are_Rotations('abc', 123)

    def test_edge_case_invalid_input3(self):
        with self.assertRaises(TypeError):
            are_Rotations(123, 456)
