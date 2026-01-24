import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_small_positive(self):
        self.assertEqual(find_lucas(2), 3)

    def test_small_negative(self):
        with self.assertRaisesRecursionLimit):
            find_lucas(-1)

    def test_large_positive(self):
        self.assertEqual(find_lucas(5), 11)

    def test_large_negative(self):
        with self.assertRaisesRecursionLimit):
            find_lucas(-5)
