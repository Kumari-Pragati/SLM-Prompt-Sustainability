import unittest
from mbpp_780_code import combinations
from 780_code import find_combinations

class TestFindCombinations(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(find_combinations([1, 2, 3, 4]), [((1, 2), (3, 4)), ((1, 3), (2, 4)), ((1, 4), (2, 3))])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(find_combinations([1]), [])
        self.assertListEqual(find_combinations([1, 2]), [((1, 2), ())])
        self.assertListEqual(find_combinations([1, 2, 2]), [((1, 2), (2,))])
        self.assertListEqual(find_combinations([1, 2, 2, 2]), [((1, 2), (2,)), ((1, 2), (2, 2)), ((1, 2, 2), ())])

    def test_special_cases(self):
        self.assertListEqual(find_combinations([1, 2, 3, 4, 5]), [((1, 2), (3, 4)), ((1, 2), (3, 5)), ((1, 2), (4, 5)),
                                                                   ((1, 3), (2, 4)), ((1, 3), (2, 5)), ((1, 3), (4, 5)),
                                                                   ((1, 4), (2, 3)), ((1, 4), (2, 5)), ((1, 4), (3, 5)],)
        self.assertListEqual(find_combinations([1, 1, 2, 3, 4]), [((1, 1), (2, 3)), ((1, 1), (2, 4)), ((1, 1), (3, 4))])
