import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(4567), 4)
        self.assertEqual(first_Digit(89012), 8)

    def test_edge_cases(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(100), 1)

    def test_boundary_cases(self):
        self.assertEqual(first_Digit(1000), 1)
        self.assertEqual(first_Digit(9999), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Digit('123')
        with self.assertRaises(TypeError):
            first_Digit(None)
