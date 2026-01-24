import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 13)
        self.assertEqual(find_star_num(3), 34)

    def test_edge_conditions(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(-1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(find_star_num(100), 6013)
        self.assertEqual(find_star_num(200), 12013)

    def test_complex_cases(self):
        self.assertEqual(find_star_num(10), 610)
        self.assertEqual(find_star_num(5), 30)
