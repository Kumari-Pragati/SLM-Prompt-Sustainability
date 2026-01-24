import unittest
from mbpp_555_code import difference

class TestDifferenceFunction(unittest.TestCase):

    def test_difference_zero(self):
        self.assertEqual(difference(0), 0)

    def test_difference_one(self):
        self.assertEqual(difference(1), 0)

    def test_difference_small_positive_numbers(self):
        for n in range(2, 6):
            self.assertEqual(difference(n), n * (n - 1))

    def test_difference_large_positive_numbers(self):
        for n in range(100, 1000, 100):
            self.assertEqual(difference(n), n * (n - 1))

    def test_difference_negative_numbers(self):
        for n in range(-100, -1, -100):
            self.assertEqual(difference(n), -n * (n + 1))
