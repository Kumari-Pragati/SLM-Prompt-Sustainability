import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('c', 'd')), ('ac', 'bd'))

    def test_edge_case_empty_tuples(self):
        self.assertEqual(concatenate_strings((), ('x', 'y')), ())
        self.assertEqual(concatenate_strings(('a',), ()), ('a',))

    def test_edge_case_single_element_tuples(self):
        self.assertEqual(concatenate_strings(('a',), ('b',)), ('ab',))
        self.assertEqual(concatenate_strings(('a',), ()), ('a',))

    def test_edge_case_mixed_length_tuples(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('c',)), ('ac', 'b'))
        self.assertEqual(concatenate_strings(('a', 'b', 'c'), ('d',)), ('ad', 'bc'))

    def test_invalid_input_non_string_elements(self):
        with self.assertRaises(TypeError):
            concatenate_strings((1, 'b'), ('c',))
        with self.assertRaises(TypeError):
            concatenate_strings(('a', 2))
