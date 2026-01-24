import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ('ghi', 'jkl')), (('abcghi', 'defjkl'),))

    def test_edge_condition(self):
        self.assertEqual(concatenate_strings(('a', ''), ('b', '')), (('ab', ''),))

    def test_boundary_condition(self):
        self.assertEqual(concatenate_strings(('a'*213, 'b'*213), ('c'*213, 'd'*213)), (('a'*426, 'b'*426),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_strings(('abc', 'def'), ('ghi', 123))
