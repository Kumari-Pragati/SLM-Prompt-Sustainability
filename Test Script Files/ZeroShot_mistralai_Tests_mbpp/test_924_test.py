import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_max_of_two_positive_numbers(self):
        self.assertEqual(max_of_two(5, 3), 5)
        self.assertEqual(max_of_two(10, 2), 10)
        self.assertEqual(max_of_two(1, 0), 1)

    def test_max_of_two_negative_numbers(self):
        self.assertEqual(max_of_two(-5, -3), -3)
        self.assertEqual(max_of_two(-10, -2), -2)
        self.assertEqual(max_of_two(-1, -10), -1)

    def test_max_of_two_zero(self):
        self.assertEqual(max_of_two(0, 5), 5)
        self.assertEqual(max_of_two(5, 0), 5)
        self.assertEqual(max_of_two(0, 0), 0)
