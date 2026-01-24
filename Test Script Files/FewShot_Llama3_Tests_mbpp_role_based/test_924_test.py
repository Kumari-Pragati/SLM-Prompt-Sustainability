import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_max_of_two_positive_numbers(self):
        self.assertEqual(max_of_two(5, 3), 5)

    def test_max_of_two_negative_numbers(self):
        self.assertEqual(max_of_two(-5, -3), -3)

    def test_max_of_two_equal_numbers(self):
        self.assertEqual(max_of_two(5, 5), 5)

    def test_max_of_two_zero(self):
        self.assertEqual(max_of_two(0, 0), 0)

    def test_max_of_two_zero_and_nonzero(self):
        self.assertEqual(max_of_two(0, 5), 5)
