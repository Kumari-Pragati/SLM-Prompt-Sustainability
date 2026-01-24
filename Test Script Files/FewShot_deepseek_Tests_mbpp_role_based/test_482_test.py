import unittest
from mbpp_482_code import match

class TestMatch(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(match('HelloWorld'), 'Yes')

    def test_edge_case(self):
        self.assertEqual(match(''), 'No')

    def test_boundary_case(self):
        self.assertEqual(match('a'), 'No')
        self.assertEqual(match('A'), 'No')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            match(123)
