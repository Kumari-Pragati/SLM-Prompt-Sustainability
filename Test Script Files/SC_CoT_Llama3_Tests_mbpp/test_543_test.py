import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_digits(123, 456), 3)
        self.assertEqual(count_digits(100, 200), 3)
        self.assertEqual(count_digits(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(count_digits(-123, 456), 3)
        self.assertEqual(count_digits(123, -456), 3)
        self.assertEqual(count_digits(0, -100), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_digits(999, 0), 4)
        self.assertEqual(count_digits(-999, 0), 4)
        self.assertEqual(count_digits(0, 999), 4)

    def test_special_cases(self):
        self.assertEqual(count_digits(123, 456), 3)
        self.assertEqual(count_digits(-123, 456), 3)
        self.assertEqual(count_digits(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_digits('123', 456)
        with self.assertRaises(TypeError):
            count_digits(123, '456')
