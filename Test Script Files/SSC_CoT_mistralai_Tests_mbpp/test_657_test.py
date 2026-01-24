import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(456), 4)
        self.assertEqual(first_Digit(789), 7)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(1000), 1)
        self.assertEqual(first_Digit(10000), 1)
        self.assertEqual(first_Digit(100000), 1)
        self.assertEqual(first_Digit(1000000), 1)
        self.assertEqual(first_Digit(10000000), 1)
        self.assertEqual(first_Digit(100000000), 1)

    def test_special_cases(self):
        self.assertEqual(first_Digit(101), 1)
        self.assertEqual(first_Digit(1011), 1)
        self.assertEqual(first_Digit(10111), 1)
        self.assertEqual(first_Digit(101111), 1)
        self.assertEqual(first_Digit(1011111), 1)
        self.assertEqual(first_Digit(10111111), 1)
        self.assertEqual(first_Digit(101111111), 1)
        self.assertEqual(first_Digit(1011111111), 1)
        self.assertEqual(first_Digit(10111111111), 1)

        self.assertEqual(first_Digit(110), 1)
        self.assertEqual(first_Digit(111), 1)
        self.assertEqual(first_Digit(1111), 1)
        self.assertEqual(first_Digit(11111), 1)
        self.assertEqual(first_Digit(111111), 1)
        self.assertEqual(first_Digit(1111111), 1)
        self.assertEqual(first_Digit(11111111), 1)
        self.assertEqual(first_Digit(111111111), 1)
        self.assertEqual(first_Digit(1111111111), 1)

        self.assertEqual(first_Digit(1234), 1)
        self.assertEqual(first_Digit(12345), 1)
        self.assertEqual(first_Digit(123456), 1)
        self.assertEqual(first_Digit(1234567), 1)
        self.assertEqual(first_Digit(12345678), 1)
        self.assertEqual(first_Digit(123456789), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, first_Digit, "string")
        self.assertRaises(TypeError, first_Digit, -1)
        self.assertRaises(TypeError, first_Digit, 0.0)
        self.assertRaises(TypeError, first_Digit, float("nan"))
        self.assertRaises(TypeError, first_Digit, complex(1, 2))
