import unittest
from mbpp_95_code import Find_Min_Length

class TestFindMinLength(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Find_Min_Length(['abc', 'defgh', 'ijklm']), 3)
        self.assertEqual(Find_Min_Length(['12345', '67', '890123']), 2)

    def test_edge_cases(self):
        self.assertEqual(Find_Min_Length(['']), 0)
        self.assertEqual(Find_Min_Length(['a']), 1)

    def test_boundary_cases(self):
        self.assertEqual(Find_Min_Length(['abcdefghijklmnop']), 16)
        self.assertEqual(Find_Min_Length(['abcdefghijklmnopqrstuvwxyz']), 26)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Find_Min_Length(123)
        with self.assertRaises(TypeError):
            Find_Min_Length(['abc', 123])
