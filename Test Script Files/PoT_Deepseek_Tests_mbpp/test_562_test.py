import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Find_Max_Length(['abc', 'defgh', 'ijklmnop']), 8)
        self.assertEqual(Find_Max_Length(['123', '456789', '0']), 7)

    def test_edge_cases(self):
        self.assertEqual(Find_Max_Length(['']), 0)
        self.assertEqual(Find_Max_Length(['a']), 1)

    def test_boundary_cases(self):
        self.assertEqual(Find_Max_Length(['abcdefghijklmnopqrstuvwxyz']), 26)
        self.assertEqual(Find_Max_Length(['a'*10000]), 10000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Find_Max_Length(123)
        with self.assertRaises(TypeError):
            Find_Max_Length(['abc', 123])
        with self.assertRaises(TypeError):
            Find_Max_Length(['abc', 'def', None])
