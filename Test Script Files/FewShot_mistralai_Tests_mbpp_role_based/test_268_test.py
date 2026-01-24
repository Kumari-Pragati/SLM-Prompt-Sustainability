import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(10), 191)

    def test_zero(self):
        self.assertEqual(find_star_num(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_star_num(-1), -7)
        self.assertEqual(find_star_num(-2), -13)
