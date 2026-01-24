import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_find_star_num(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(3), 13)
        self.assertEqual(find_star_num(4), 22)
        self.assertEqual(find_star_num(5), 34)
        self.assertEqual(find_star_num(6), 49)
        self.assertEqual(find_star_num(7), 67)
        self.assertEqual(find_star_num(8), 86)
        self.assertEqual(find_star_num(9), 108)
        self.assertEqual(find_star_num(10), 133)
