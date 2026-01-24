import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(split_upperstring('HelloWorldThisIsATest'), ['Hello', 'World', 'This', 'Is', 'A', 'Test'])

    def test_edge_condition(self):
        self.assertEqual(split_upperstring('A'), ['A'])

    def test_boundary_condition(self):
        self.assertEqual(split_upperstring(''), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_upperstring(123)
