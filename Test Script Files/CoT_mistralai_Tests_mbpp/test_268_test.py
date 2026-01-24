import unittest
from mbpp_268_code import find_star_num

class TestFindStarNum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_star_num(1), 1)
        self.assertEqual(find_star_num(2), 7)
        self.assertEqual(find_star_num(3), 19)
        self.assertEqual(find_star_num(10), 211)

    def test_zero(self):
        self.assertEqual(find_star_num(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(find_star_num(-1), None)
        self.assertEqual(find_star_num(-2), None)

    def test_large_numbers(self):
        self.assertEqual(find_star_num(1000), 6000000001)
        self.assertEqual(find_star_num(1000000), 5999999999999999999)
