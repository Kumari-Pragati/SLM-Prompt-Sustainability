import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_two(self):
        self.assertEqual(find_lucas(2), 3)

    def test_three(self):
        self.assertEqual(find_lucas(3), 4)

    def test_four(self):
        self.assertEqual(find_lucas(4), 7)

    def test_five(self):
        self.assertEqual(find_lucas(5), 11)

    def test_negative(self):
        with self.assertRaises(TypeError):
            find_lucas(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_lucas('a')
