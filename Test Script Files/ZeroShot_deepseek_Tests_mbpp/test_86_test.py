import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 19)
        self.assertEqual(centered_hexagonal_number(4), 37)
        self.assertEqual(centered_hexagonal_number(5), 61)

    def test_zero(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(centered_hexagonal_number(-1), 1)
        self.assertEqual(centered_hexagonal_number(-2), 1)
        self.assertEqual(centered_hexagonal_number(-3), 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(2.5)

    def test_large_numbers(self):
        self.assertEqual(centered_hexagonal_number(100), 5995)
