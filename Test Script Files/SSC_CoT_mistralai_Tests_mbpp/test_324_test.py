import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_normal_input(self):
        self.assertTupleEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((1 + 3), (2 + 4)))
        self.assertTupleEqual(sum_of_alternates((5, 4, 3, 2, 1)), ((5 + 3), (4 + 2)))

    def test_edge_cases(self):
        self.assertTupleEqual(sum_of_alternates((1)), ((1, 0)))
        self.assertTupleEqual(sum_of_alternates((1, 2)), ((1, 2)))
        self.assertTupleEqual(sum_of_alternates((1, 2, 3)), ((1 + 3, 2)))
        self.assertTupleEqual(sum_of_alternates((1, 2, 3, 4, 5, 6)), ((1 + 3 + 5), (2 + 4)))

    def test_empty_list(self):
        self.assertTupleEqual(sum_of_alternates([]), ((0, 0)))

    def test_negative_numbers(self):
        self.assertTupleEqual(sum_of_alternates((-1, 0, 1)), ((-1 + 1, 0)))
        self.assertTupleEqual(sum_of_alternates((-1, 0, 1, -2)), ((-1 + 1, 0 + 1 - 2)))
