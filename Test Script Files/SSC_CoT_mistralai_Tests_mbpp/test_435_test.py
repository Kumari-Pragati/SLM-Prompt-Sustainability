import unittest
from mbpp_435_code import last_Digit

class TestLastDigit(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(last_Digit(12345), 5)
        self.assertEqual(last_Digit(-12345), 5)
        self.assertEqual(last_Digit(0), 0)

    def test_edge_cases(self):
        self.assertEqual(last_Digit(1000000000), 0)
        self.assertEqual(last_Digit(-1000000000), 0)
        self.assertEqual(last_Digit(999999999), 9)
        self.assertEqual(last_Digit(-999999999), 9)

    def test_negative_numbers(self):
        self.assertEqual(last_Digit(-1), -1)
        self.assertEqual(last_Digit(-123), 3)
        self.assertEqual(last_Digit(-1230), 0)

    def test_floats(self):
        self.assertEqual(last_Digit(123.456), 6)
        self.assertEqual(last_Digit(-123.456), 6)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, last_Digit, 'abc')
        self.assertRaises(TypeError, last_Digit, (1, 2, 3))
