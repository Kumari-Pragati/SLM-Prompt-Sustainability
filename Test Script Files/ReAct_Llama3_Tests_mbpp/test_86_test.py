import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 5)
        self.assertEqual(centered_hexagonal_number(3), 12)
        self.assertEqual(centered_hexagonal_number(4), 22)
        self.assertEqual(centered_hexagonal_number(5), 35)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(-1)

    def test_zero(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            centered_hexagonal_number(1.5)
