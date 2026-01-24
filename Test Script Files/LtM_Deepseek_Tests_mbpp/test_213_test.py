import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('c', 'd')), (('ac', 'bd')))

    def test_edge_conditions(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('', '')), (('', '')))
        self.assertEqual(concatenate_strings(('a', ''), ('c', 'd')), (('ac', 'd')))
        self.assertEqual(concatenate_strings(('', 'b'), ('c', 'd')), (('cd', 'bd')))

    def test_boundary_conditions(self):
        self.assertEqual(concatenate_strings(('a'*213, 'b'*213), ('c'*213, 'd'*213)), (('a'*213+'c'*213, 'b'*213+'d'*213)))

    def test_complex_cases(self):
        self.assertEqual(concatenate_strings(('a', 'b', 'c'), ('d', 'e', 'f')), (('ad', 'be', 'cf')))
