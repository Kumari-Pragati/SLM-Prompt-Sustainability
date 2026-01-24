import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(1), 1)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(15), 17)

    def test_edge(self):
        self.assertEqual(decimal_to_Octal(16), 20)
        self.assertEqual(decimal_to_Octal(17), 21)
        self.assertEqual(decimal_to_Octal(24), 30)
        self.assertEqual(decimal_to_Octal(25), 31)
        self.assertEqual(decimal_to_Octal(32), 40)

    def test_complex(self):
        self.assertEqual(decimal_to_Octal(100), 144)
        self.assertEqual(decimal_to_Octal(101), 145)
        self.assertEqual(decimal_to_Octal(102), 146)
        self.assertEqual(decimal_to_Octal(103), 147)
        self.assertEqual(decimal_to_Octal(104), 148)
