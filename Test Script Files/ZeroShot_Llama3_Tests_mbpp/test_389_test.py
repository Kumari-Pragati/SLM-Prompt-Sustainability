import unittest
from mbpp_389_code import find_lucas

class TestFindLucas(unittest.TestCase):

    def test_find_lucas_zero(self):
        self.assertEqual(find_lucas(0), 2)

    def test_find_lucas_one(self):
        self.assertEqual(find_lucas(1), 1)

    def test_find_lucas_two(self):
        self.assertEqual(find_lucas(2), 2)

    def test_find_lucas_three(self):
        self.assertEqual(find_lucas(3), 3)

    def test_find_lucas_four(self):
        self.assertEqual(find_lucas(4), 4)

    def test_find_lucas_five(self):
        self.assertEqual(find_lucas(5), 5)

    def test_find_lucas_six(self):
        self.assertEqual(find_lucas(6), 8)

    def test_find_lucas_seven(self):
        self.assertEqual(find_lucas(7), 11)

    def test_find_lucas_eight(self):
        self.assertEqual(find_lucas(8), 18)

    def test_find_lucas_nine(self):
        self.assertEqual(find_lucas(9), 29)

    def test_find_lucas_ten(self):
        self.assertEqual(find_lucas(10), 47)
