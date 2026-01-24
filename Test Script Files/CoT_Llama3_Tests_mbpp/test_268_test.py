import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(3), 13)
        self.assertEqual(find_star_num(4), 22)
        self.assertEqual(find_star_num(5), 34)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(-1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_star_num('a')
        with self.assertRaises(TypeError):
            find_star_num(None)
