import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(2), 2)
        self.assertEqual(first_Digit(3), 6)
        self.assertEqual(first_Digit(4), 24)
        self.assertEqual(first_Digit(5), 120)

    def test_edge_conditions(self):
        self.assertEqual(first_Digit(0), 1)
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(2), 2)
        self.assertEqual(first_Digit(10), 3628800)

    def test_boundary_conditions(self):
        self.assertEqual(first_Digit(11), 39916800)
        self.assertEqual(first_Digit(20), 2432902008176640000)

    def test_complex_cases(self):
        self.assertEqual(first_Digit(30), 265252859812191058636308480000000)
