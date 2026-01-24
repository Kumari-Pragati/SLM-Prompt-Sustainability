import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(first_Digit(12), 1)
        self.assertEqual(first_Digit(98), 9)
        self.assertEqual(first_Digit(314), 3)
        self.assertEqual(first_Digit(5678), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(9), 9)
        self.assertEqual(first_Digit(10), 1)
        self.assertEqual(first_Digit(99), 9)
        self.assertEqual(first_Digit(100), 1)
