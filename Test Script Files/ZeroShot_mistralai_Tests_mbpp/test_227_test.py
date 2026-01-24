import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_min_of_three_positive_numbers(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(3, 2, 1), 1)
        self.assertEqual(min_of_three(2, 1, 3), 1)
        self.assertEqual(min_of_three(1, 1, 3), 1)
        self.assertEqual(min_of_three(1, 3, 1), 1)
        self.assertEqual(min_of_three(3, 1, 1), 1)

    def test_min_of_three_zero_and_positive_numbers(self):
        self.assertEqual(min_of_three(0, 2, 3), 0)
        self.assertEqual(min_of_three(2, 0, 3), 0)
        self.assertEqual(min_of_three(2, 3, 0), 0)
        self.assertEqual(min_of_three(0, 0, 3), 0)
        self.assertEqual(min_of_three(0, 3, 0), 0)
        self.assertEqual(min_of_three(3, 0, 0), 0)

    def test_min_of_three_negative_numbers(self):
        self.assertEqual(min_of_three(-1, -2, -3), -1)
        self.assertEqual(min_of_three(-3, -2, -1), -3)
        self.assertEqual(min_of_three(-2, -1, -3), -3)
        self.assertEqual(min_of_three(-1, -1, -3), -1)
        self.assertEqual(min_of_three(-1, -3, -1), -3)
        self.assertEqual(min_of_three(-3, -1, -1), -3)

    def test_min_of_three_zero_and_negative_numbers(self):
        self.assertEqual(min_of_three(0, -2, -3), -3)
        self.assertEqual(min_of_three(-2, 0, -3), -3)
        self.assertEqual(min_of_three(-2, -3, 0), -3)
        self.assertEqual(min_of_three(0, 0, -3), -3)
        self.assertEqual(min_of_three(0, -3, 0), -3)
        self.assertEqual(min_of_three(-3, 0, 0), -3)
