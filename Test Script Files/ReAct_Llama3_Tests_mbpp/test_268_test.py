import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(find_star_num(0), 1)

    def test_positive_input(self):
        self.assertEqual(find_star_num(1), 7)
        self.assertEqual(find_star_num(2), 13)
        self.assertEqual(find_star_num(3), 23)
        self.assertEqual(find_star_num(4), 37)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            find_star_num(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            find_star_num('a')

    def test_edge_case(self):
        self.assertEqual(find_star_num(100), 3961)
