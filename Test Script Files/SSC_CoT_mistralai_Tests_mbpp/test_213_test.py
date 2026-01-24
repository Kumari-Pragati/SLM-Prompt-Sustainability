import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('c', 'd')), ('ac', 'bd'))
        self.assertEqual(concatenate_strings(('A', 'B'), ('C', 'D')), ('AC', 'BD'))
        self.assertEqual(concatenate_strings(('1', '2'), ('3', '4')), ('13', '24'))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(concatenate_strings(('a',), ('b',)), ('ab',))
        self.assertEqual(concatenate_strings((), ('b',)), (None,))
        self.assertEqual(concatenate_strings(('a',), ('',)), ('a',))
        self.assertEqual(concatenate_strings(('',), ('b',)), (None,))

    def test_special_inputs(self):
        self.assertEqual(concatenate_strings(('a', 'b'), ('1', '2')), ('a1', 'b2'))
        self.assertEqual(concatenate_strings(('a', 'b'), ('1', '2.0')), ('a1', 'b2.0'))
