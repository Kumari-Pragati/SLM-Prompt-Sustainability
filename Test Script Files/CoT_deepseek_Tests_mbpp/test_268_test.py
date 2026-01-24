import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_star_num(5), 149)

    def test_zero_input(self):
        self.assertEqual(find_star_num(0), 1)

    def test_negative_input(self):
        with self.assertRaises(Exception):
            find_star_num(-1)

    def test_large_input(self):
        self.assertEqual(find_star_num(1000), 600049)
