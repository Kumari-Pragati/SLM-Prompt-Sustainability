import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(centered_hexagonal_number(5), 86)

    def test_small_number(self):
        self.assertEqual(centered_hexagonal_number(1), 1)

    def test_large_number(self):
        self.assertEqual(centered_hexagonal_number(10), 301)

    def test_zero(self):
        self.assertEqual(centered_hexagonal_number(0), 1)

    def test_negative_number(self):
        with self.assertRaises(Exception):
            centered_hexagonal_number(-1)

    def test_non_integer_input(self):
        with self.assertRaises(Exception):
            centered_hexagonal_number(1.5)
