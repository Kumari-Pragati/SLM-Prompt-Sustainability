import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_small(self):
        self.assertEqual(find_lucas(2), 3)

    def test_medium(self):
        self.assertEqual(find_lucas(3), 4)

    def test_large(self):
        self.assertEqual(find_lucas(4), 7)

    def test_negative(self):
        with self.assertRaisesRecursionLimitError:
            find_lucas(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_lucas(3.5)
