import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(first_Digit(123), 1)
        self.assertEqual(first_Digit(4567), 4)
        self.assertEqual(first_Digit(98765), 9)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(9), 9)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(99), 9)
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(999), 9)
        self.assertEqual(first_Digit(1000), 1)

    def test_special_cases(self):
        self.assertEqual(first_Digit(10000), 1)
        self.assertEqual(first_Digit(100000), 1)
        self.assertEqual(first_Digit(1000000), 1)
        self.assertEqual(first_Digit(10000000), 1)
        self.assertEqual(first_Digit(100000000), 1)
        self.assertEqual(first_Digit(1000000000), 1)
