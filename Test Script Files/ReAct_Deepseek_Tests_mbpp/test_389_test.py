import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_positive_numbers(self):
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)
        self.assertEqual(find_lucas(5), 11)

    def test_negative_numbers(self):
        with self.assertRaises(RecursionError):
            find_lucas(-1)

    def test_large_numbers(self):
        # This test may take a while to run
        self.assertEqual(find_lucas(10), 123)
