import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_centered_hexagonal_number_with_positive_integer(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 23)
        self.assertEqual(centered_hexagonal_number(4), 49)
        self.assertEqual(centered_hexagonal_number(5), 99)
        self.assertEqual(centered_hexagonal_number(6), 171)
        self.assertEqual(centered_hexagonal_number(7), 267)
        self.assertEqual(centered_hexagonal_number(8), 393)
        self.assertEqual(centered_hexagonal_number(9), 551)
        self.assertEqual(centered_hexagonal_number(10), 743)

    def test_centered_hexagonal_number_with_zero(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_centered_hexagonal_number_with_negative_integer(self):
        self.assertRaises(ValueError, centered_hexagonal_number, -1)
        self.assertRaises(ValueError, centered_hexagonal_number, -2)
        self.assertRaises(ValueError, centered_hexagonal_number, -3)
