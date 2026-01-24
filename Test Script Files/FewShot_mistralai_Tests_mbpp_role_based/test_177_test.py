import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(2, 4), (2, 4))
        self.assertEqual(answer(3, 6), (3, 6))

    def test_zero(self):
        self.assertEqual(answer(0, 0), (-1))

    def test_negative_numbers(self):
        self.assertEqual(answer(-1, 0), (-1))
        self.assertEqual(answer(-2, -4), (-1))
        self.assertEqual(answer(-3, -6), (-1))

    def test_negative_and_positive(self):
        self.assertEqual(answer(-1, 1), (-1))
        self.assertEqual(answer(-2, 2), (-1))
        self.assertEqual(answer(-3, 3), (-1))
