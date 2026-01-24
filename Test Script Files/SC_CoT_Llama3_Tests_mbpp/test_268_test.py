import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 11)
        self.assertEqual(find_star_num(3), 53)

    def test_edge_cases(self):
        self.assertEqual(find_star_num(0), 1)
        self.assertEqual(find_star_num(-1), 1)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            find_star_num(-2)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            find_star_num(2.5)

    def test_large_inputs(self):
        self.assertEqual(find_star_num(100), 678271)
