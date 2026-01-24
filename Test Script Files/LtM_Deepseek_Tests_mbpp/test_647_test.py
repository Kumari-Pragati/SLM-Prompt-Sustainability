import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(split_upperstring('A'), ['A'])
        self.assertEqual(split_upperstring('AB'), ['AB'])
        self.assertEqual(split_upperstring('ABC'), ['ABC'])

    def test_edge_conditions(self):
        self.assertEqual(split_upperstring(''), [])
        self.assertEqual(split_upperstring('a'), [])
        self.assertEqual(split_upperstring('123'), [])
        self.assertEqual(split_upperstring('A1B2C3'), ['A1B2C3'])

    def test_complex_cases(self):
        self.assertEqual(split_upperstring('A1B2C3'), ['A1B2C3'])
        self.assertEqual(split_upperstring('A1B2C3D4E5F6'), ['A1B2C3', 'D4E5F6'])
        self.assertEqual(split_upperstring('ABCDEF'), ['ABCDEF'])
        self.assertEqual(split_upperstring('ABCDEFGHI'), ['ABCDEF', 'GHI'])
