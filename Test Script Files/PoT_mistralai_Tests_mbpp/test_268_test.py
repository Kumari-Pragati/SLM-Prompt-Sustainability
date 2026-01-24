import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_star_num(3), 23)
        self.assertEqual(find_star_num(4), 49)
        self.assertEqual(find_star_num(5), 85)

    def test_edge_case(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(1), 7)
        self.assertEqual(find_star_num(2), 23)
        self.assertEqual(find_star_num(6), 121)
        self.assertEqual(find_star_num(7), 187)

    def test_boundary_case(self):
        self.assertEqual(find_star_num(100), 60001)
        self.assertEqual(find_star_num(1000), 6000001)
