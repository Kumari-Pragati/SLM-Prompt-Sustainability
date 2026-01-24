import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(split_upperstring('HelloWORLD'), ['Hello', 'WORLD'])

    def test_edge_case(self):
        self.assertEqual(split_upperstring('A'), ['A'])
        self.assertEqual(split_upperstring(''), [])

    def test_corner_case(self):
        self.assertEqual(split_upperstring('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
        self.assertEqual(split_upperstring('aBCdefghijklmnopqrstuvwxyz'), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_upperstring(123)
