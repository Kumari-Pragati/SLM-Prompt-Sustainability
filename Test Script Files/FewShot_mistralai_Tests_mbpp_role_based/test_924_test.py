import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(3, 5), 5)

    def test_zero(self):
        self.assertEqual(max_of_two(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(max_of_two(-5, -3), -3)
        self.assertEqual(max_of_two(-3, -5), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_of_two(-5, 3), 3)
        self.assertEqual(max_of_two(3, -5), 3)
