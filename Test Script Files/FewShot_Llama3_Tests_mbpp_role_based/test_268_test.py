import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(find_star_num(1), 1)

    def test_large_positive_integer(self):
        self.assertEqual(find_star_num(100), 600099)

    def test_zero(self):
        with self.assertRaises(TypeError):
            find_star_num(0)

    def test_negative_integer(self):
        with self.assertRaises(TypeError):
            find_star_num(-1)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            find_star_num('a')
