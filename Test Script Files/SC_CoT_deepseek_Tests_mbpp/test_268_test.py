import unittest

from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_star_num(5), 145)

    def test_boundary_case(self):
        self.assertEqual(find_star_num(1), 1)

    def test_edge_case(self):
        self.assertEqual(find_star_num(0), 1)

    def test_negative_case(self):
        with self.assertRaises(ValueError):
            find_star_num(-1)
