import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_typical_use_cases(self):
        self.assertEqual(first_Digit(5), 1)
        self.assertEqual(first_Digit(10), 3)
        self.assertEqual(first_Digit(20), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(first_Digit(0), 1)
        self.assertEqual(first_Digit(1), 1)
        self.assertEqual(first_Digit(2), 2)
        self.assertEqual(first_Digit(10), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Digit('a')
        with self.assertRaises(ValueError):
            first_Digit(-5)
