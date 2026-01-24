import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)
        self.assertEqual(count_Hexadecimal(16, 20), 1)
        self.assertEqual(count_Hexadecimal(100, 110), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Hexadecimal(0, 0), 0)
        self.assertEqual(count_Hexadecimal(10, 10), 1)
        self.assertEqual(count_Hexadecimal(15, 15), 1)
        self.assertEqual(count_Hexadecimal(16, 16), 1)
        self.assertEqual(count_Hexadecimal(20, 20), 0)

    def test_explicitly_handled_error_cases(self):
        self.assertEqual(count_Hexadecimal(-10, 10), 6)
        self.assertEqual(count_Hexadecimal(10, -10), 6)
        self.assertEqual(count_Hexadecimal(-10, -10), 0)
