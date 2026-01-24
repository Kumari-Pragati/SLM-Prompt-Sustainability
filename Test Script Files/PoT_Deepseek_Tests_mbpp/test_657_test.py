import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(first_Digit(5), 1)
        self.assertEqual(first_Digit(10), 3)
        self.assertEqual(first_Digit(15), 1)
        self.assertEqual(first_Digit(20), 2)

    def test_edge_cases(self):
        self.assertEqual(first_Digit(0), 1)
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(2), 2)

    def test_boundary_cases(self):
        self.assertEqual(first_Digit(100), 1)
        self.assertEqual(first_Digit(1000), 1)
        self.assertEqual(first_Digit(10000), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Digit('a')
        with self.assertRaises(ValueError):
            first_Digit(-5)
