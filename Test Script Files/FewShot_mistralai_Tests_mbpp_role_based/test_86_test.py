import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 19)
        self.assertEqual(centered_hexagonal_number(4), 37)
        self.assertEqual(centered_hexagonal_number(5), 61)

    def test_zero(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative_integer(self):
        self.assertRaises(ValueError, centered_hexagonal_number, -1)
        self.assertRaises(ValueError, centered_hexagonal_number, -2)
