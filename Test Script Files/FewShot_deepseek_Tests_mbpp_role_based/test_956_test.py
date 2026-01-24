import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(split_list('A1B2C3D4'), ['A1', 'B2', 'C3', 'D4'])

    def test_edge_condition(self):
        self.assertEqual(split_list('A'), ['A'])

    def test_boundary_condition(self):
        self.assertEqual(split_list('ABCD'), ['AB', 'CD'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_list(123)
