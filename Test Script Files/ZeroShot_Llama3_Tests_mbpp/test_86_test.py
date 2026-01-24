import unittest
from mbpp_86_code import centered_hexagonal_number

class TestCenteredHexagonalNumber(unittest.TestCase):

    def test_centered_hexagonal_number(self):
        self.assertEqual(centered_hexagonal_number(1), 1)
        self.assertEqual(centered_hexagonal_number(2), 7)
        self.assertEqual(centered_hexagonal_number(3), 18)
        self.assertEqual(centered_hexagonal_number(4), 36)
        self.assertEqual(centered_hexagonal_number(5), 65)
        self.assertEqual(centered_hexagonal_number(6), 111)
        self.assertEqual(centered_hexagonal_number(7), 175)
        self.assertEqual(centered_hexagonal_number(8), 265)
        self.assertEqual(centered_hexagonal_number(9), 386)
        self.assertEqual(centered_hexagonal_number(10), 526)
