import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(find_combinations([1, 2, 3]), [(2, 3), (1, 2), (1, 3)])
        self.assertListEqual(find_combinations([4, 5, 6]), [(5, 6), (4, 5), (4, 6)])

    def test_edge_cases(self):
        self.assertListEqual(find_combinations([1]), [])
        self.assertListEqual(find_combinations([1, 2]), [(2, 1)])
        self.assertListEqual(find_combinations([1, 2, 3, 4]), [(2, 3), (3, 4), (4, 1), (1, 2)])

    def test_complex(self):
        self.assertListEqual(find_combinations([1, 2, 3, 4, 5]), [(2, 3), (3, 4), (4, 5), (5, 1), (1, 2)])
        self.assertListEqual(find_combinations([10, 20, 30, 40, 50]), [(20, 30), (30, 40), (40, 50), (50, 10), (10, 20)])
