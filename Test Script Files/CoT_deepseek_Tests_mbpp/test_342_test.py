import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_typical_case(self):
        list = [[4, 7, 9, 10], [2, 3, 6, 8], [1, 5, 11, 12]]
        self.assertEqual(find_minimum_range(list), (1, 2))

    def test_single_list(self):
        list = [[1, 2, 3, 4]]
        self.assertEqual(find_minimum_range(list), (1, 4))

    def test_empty_list(self):
        list = []
        self.assertEqual(find_minimum_range(list), None)

    def test_single_value(self):
        list = [[1]]
        self.assertEqual(find_minimum_range(list), (1, 1))

    def test_negative_values(self):
        list = [[-1, -2, -3, -4], [-5, -6, -7, -8], [-9, -10, -11, -12]]
        self.assertEqual(find_minimum_range(list), (-9, -10))

    def test_duplicate_values(self):
        list = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        self.assertEqual(find_minimum_range(list), (1, 1))

    def test_large_numbers(self):
        list = [[1000000, 2000000, 3000000, 4000000], [500000, 600000, 700000, 800000], [900000, 1000000, 1100000, 1200000]]
        self.assertEqual(find_minimum_range(list), (500000, 1200000))
