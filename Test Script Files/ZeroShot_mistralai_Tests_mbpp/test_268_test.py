import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_find_star_num_positive(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 3)
        self.assertEqual(find_star_num(3), 7)
        self.assertEqual(find_star_num(4), 11)
        self.assertEqual(find_star_num(5), 15)

    def test_find_star_num_zero(self):
        self.assertEqual(find_star_num(0), 0)

    def test_find_star_num_negative(self):
        self.assertEqual(find_star_num(-1), None)
        self.assertEqual(find_star_num(-2), None)
        self.assertEqual(find_star_num(-3), None)
