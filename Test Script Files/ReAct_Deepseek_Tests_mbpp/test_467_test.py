import unittest
from mbpp_467_code import decimal_to_Octal

class TestDecimalToOctal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(decimal_to_Octal(10), 12)
        self.assertEqual(decimal_to_Octal(20), 24)
        self.assertEqual(decimal_to_Octal(100), 144)

    def test_edge_cases(self):
        self.assertEqual(decimal_to_Octal(0), 0)
        self.assertEqual(decimal_to_Octal(8), 10)
        self.assertEqual(decimal_to_Octal(64), 100)

    def test_explicitly_handled_error_cases(self):
        # Since the function does not handle any error cases, 
        # this test is just to ensure that the function does not throw an error
        self.assertIsNone(decimal_to_Octal(-10))
        self.assertIsNone(decimal_to_Octal(10.5))
        self.assertIsNone(decimal_to_Octal('abc'))
