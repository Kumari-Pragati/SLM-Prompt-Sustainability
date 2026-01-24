import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_digits(123, 456), 6)
        self.assertEqual(count_digits(0, 987), 3)
        self.assertEqual(count_digits(1000, 2000), 4)

    def test_edge_cases(self):
        self.assertEqual(count_digits(0, 0), 1)
        self.assertEqual(count_digits(1, 0), 1)
        self.assertEqual(count_digits(0, -1), 1)
        self.assertEqual(count_digits(-1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_digits(9, 9), 2)
        self.assertEqual(count_digits(99, 99), 3)
        self.assertEqual(count_digits(999, 999), 4)
        self.assertEqual(count_digits(-9, -9), 2)
        self.assertEqual(count_digits(-99, -99), 3)
        self.assertEqual(count_digits(-999, -999), 4)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_digits, '123', 456)
        self.assertRaises(TypeError, count_digits, 123, '456')
