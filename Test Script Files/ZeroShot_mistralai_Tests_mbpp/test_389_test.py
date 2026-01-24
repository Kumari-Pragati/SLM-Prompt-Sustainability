import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):
    def test_find_lucas_with_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_find_lucas_with_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_find_lucas_with_positive_number(self):
        self.assertEqual(find_lucas(2), 3)
        self.assertEqual(find_lucas(3), 4)
        self.assertEqual(find_lucas(4), 7)
        self.assertEqual(find_lucas(5), 11)
        self.assertEqual(find_lucas(6), 18)

    def test_find_lucas_with_negative_number(self):
        self.assertEqual(find_lucas(-1), TracebackError)
