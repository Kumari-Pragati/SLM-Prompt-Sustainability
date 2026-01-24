import unittest
from mbpp_657_code import first_Digit

class TestFirstDigit(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(first_Digit(1), 0)
        self.assertEqual(first_Digit(2), 1)
        self.assertEqual(first_Digit(3), 1)
        self.assertEqual(first_Digit(4), 2)
        self.assertEqual(first_Digit(5), 2)
        self.assertEqual(first_Digit(6), 3)
        self.assertEqual(first_Digit(7), 3)
        self.assertEqual(first_Digit(8), 4)
        self.assertEqual(first_Digit(9), 4)
        self.assertEqual(first_Digit(10), 5)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(first_Digit(0), 0)
        self.assertEqual(first_Digit(1), 0)
        self.assertEqual(first_Digit(2), 1)
        self.assertEqual(first_Digit(3), 1)
        self.assertEqual(first_Digit(4), 2)
        self.assertEqual(first_Digit(5), 2)
        self.assertEqual(first_Digit(6), 3)
        self.assertEqual(first_Digit(7), 3)
        self.assertEqual(first_Digit(8), 4)
        self.assertEqual(first_Digit(9), 4)
        self.assertEqual(first_Digit(10), 5)
        self.assertEqual(first_Digit(11), 5)
        self.assertEqual(first_Digit(12), 6)

    def test_special_and_corner_cases(self):
        self.assertEqual(first_Digit(20), 4)
        self.assertEqual(first_Digit(30), 5)
        self.assertEqual(first_Digit(40), 6)
        self.assertEqual(first_Digit(50), 7)
        self.assertEqual(first_Digit(60), 8)
        self.assertEqual(first_Digit(70), 9)
        self.assertEqual(first_Digit(80), 10)
        self.assertEqual(first_Digit(90), 11)
        self.assertEqual(first_Digit(100), 12)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            first_Digit('a')
        with self.assertRaises(TypeError):
            first_Digit(None)
