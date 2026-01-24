import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(456), 4)
        self.assertEqual(first_Digit(789), 7)

    def test_edge_cases(self):
        self.assertEqual(first_Digit(9), 9)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(99), 9)
        self.assertEqual(first_Digit(100), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Digit('abc')
        with self.assertRaises(TypeError):
            first_Digit(None)
