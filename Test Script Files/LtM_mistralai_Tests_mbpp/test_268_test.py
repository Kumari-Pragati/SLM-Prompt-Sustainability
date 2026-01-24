import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(find_star_num(1), 3)
        self.assertEqual(find_star_num(2), 13)
        self.assertEqual(find_star_num(3), 29)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(1000), 6000001)
        self.assertEqual(find_star_num(-1), None)
