import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 13)
        self.assertEqual(find_star_num(3), 34)
        self.assertEqual(find_star_num(4), 61)

    def test_edge_cases(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(-1), 1)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            find_star_num('a')
        with self.assertRaises(ValueError):
            find_star_num(-2)
