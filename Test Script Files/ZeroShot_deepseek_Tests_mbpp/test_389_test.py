import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_find_lucas_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_find_lucas_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_find_lucas_positive(self):
        self.assertEqual(find_lucas(5), 11)

    def test_find_lucas_negative(self):
        with self.assertRaises(RecursionError):
            find_lucas(-1)

    def test_find_lucas_large(self):
        with self.assertRaises(RecursionError):
            find_lucas(30)
