import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_small_positive_numbers(self):
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)

    def test_large_positive_numbers(self):
        self.assertEqual(find_lucas(10), 29)
        self.assertEqual(find_lucas(20), 121)
        self.assertEqual(find_lucas(30), 364)

    def test_negative_numbers(self):
        self.assertEqual(find_lucas(-1), None)
        self.assertEqual(find_lucas(-2), None)
