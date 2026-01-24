import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(3), 26)

    def test_edge_case(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(-1), 1)

    def test_boundary_case(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(100), 600099)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_star_num('a')
