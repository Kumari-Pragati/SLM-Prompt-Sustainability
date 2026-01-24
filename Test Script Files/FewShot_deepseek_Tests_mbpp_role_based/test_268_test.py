import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_star_num(5), 149)

    def test_boundary_conditions(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(1), 1)

    def test_edge_conditions(self):
        self.assertEqual(find_star_num(-1), 1)
        self.assertEqual(find_star_num(2), 15)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_star_num('a')
        with self.assertRaises(ValueError):
            find_star_num(None)
