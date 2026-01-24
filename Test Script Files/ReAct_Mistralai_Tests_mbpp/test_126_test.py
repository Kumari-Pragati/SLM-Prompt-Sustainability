import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum(4, 6), 2)
        self.assertEqual(sum(6, 8), 6)
        self.assertEqual(sum(8, 10), 8)

    def test_zero_and_positive_number(self):
        self.assertEqual(sum(0, 4), 0)
        self.assertEqual(sum(4, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum(-4, -6), 4)
        self.assertEqual(sum(-6, -8), 6)
        self.assertEqual(sum(-8, -10), 8)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(sum(-4, 4), 0)
        self.assertEqual(sum(4, -4), 0)

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            sum(12)

    def test_zero_arguments(self):
        with self.assertRaises(TypeError):
            sum()

    def test_non_integer_arguments(self):
        with self.assertRaises(TypeError):
            sum(4.0, 6.0)

    def test_large_numbers(self):
        self.assertEqual(sum(1000000, 1000000), 1000000)

    def test_small_numbers(self):
        self.assertEqual(sum(1, 2), 1)
