import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(456), 4)
        self.assertEqual(first_Digit(789), 7)

    def test_edge_cases(self):
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(100), 1)

    def test_large_numbers(self):
        self.assertEqual(first_Digit(1000), 1)
        self.assertEqual(first_Digit(10000), 1)
        self.assertEqual(first_Digit(100000), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Digit('abc')
        with self.assertRaises(TypeError):
            first_Digit(None)
