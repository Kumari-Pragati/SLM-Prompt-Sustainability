import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 13)
        self.assertEqual(find_star_num(3), 34)

    def test_edge_cases(self):
        self.assertEqual(find_star_num(0), 1)

    def test_corner_cases(self):
        self.assertEqual(find_star_num(10), 601)
        self.assertEqual(find_star_num(100), 60101)
