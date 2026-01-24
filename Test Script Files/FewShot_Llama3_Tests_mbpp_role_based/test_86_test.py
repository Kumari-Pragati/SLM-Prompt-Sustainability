import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 18)
        self.assertEqual(centered_hexagonal_number(4), 34)
        self.assertEqual(centered_hexagonal_number(5), 55)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(-1)

    def test_zero(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(0)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(1.5)
