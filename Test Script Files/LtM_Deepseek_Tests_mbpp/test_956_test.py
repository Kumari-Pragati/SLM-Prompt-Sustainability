import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(split_list('A'), ['A'])
        self.assertEqual(split_list('AB'), ['AB'])
        self.assertEqual(split_list('ABC'), ['ABC'])

    def test_edge_conditions(self):
        self.assertEqual(split_list(''), [])
        self.assertEqual(split_list('A1B2C3'), ['A1B2C3'])
        self.assertEqual(split_list('123456'), [])

    def test_complex_cases(self):
        self.assertEqual(split_list('A1B2C3'), ['A1B2C3'])
        self.assertEqual(split_list('ABCDEF'), ['ABCDEF'])
        self.assertEqual(split_list('A1B2C3D4E5F6'), ['A1B2C3D4E5F6'])
