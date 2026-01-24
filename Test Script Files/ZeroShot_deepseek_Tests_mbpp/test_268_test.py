import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_find_star_num_positive(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 13)
        self.assertEqual(find_star_num(3), 37)
        self.assertEqual(find_star_num(4), 73)
        self.assertEqual(find_star_num(5), 121)

    def test_find_star_num_zero(self):
        self.assertEqual(find_star_num(0), 1)

    def test_find_star_num_negative(self):
        self.assertEqual(find_star_num(-1), 1)
        self.assertEqual(find_star_num(-2), 1)
        self.assertEqual(find_star_num(-3), 1)
