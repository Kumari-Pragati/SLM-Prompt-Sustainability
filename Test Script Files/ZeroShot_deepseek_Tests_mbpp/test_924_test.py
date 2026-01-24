import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_max_of_two_positive_numbers(self):
        self.assertEqual(max_of_two(10, 20), 20)

    def test_max_of_two_negative_numbers(self):
        self.assertEqual(max_of_two(-10, -20), -10)

    def test_max_of_two_equal_numbers(self):
        self.assertEqual(max_of_two(10, 10), 10)

    def test_max_of_two_one_negative_number(self):
        self.assertEqual(max_of_two(-10, 20), 20)

    def test_max_of_two_zero_and_positive(self):
        self.assertEqual(max_of_two(0, 20), 20)

    def test_max_of_two_zero_and_negative(self):
        self.assertEqual(max_of_two(0, -20), 0)
