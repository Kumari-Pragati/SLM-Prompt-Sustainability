import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(3), 13)

    def test_edge_cases(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(-1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_star_num('a')
