import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((1, 2, 3, 4), (5)))
        self.assertEqual(sum_of_alternates((5, 4, 3, 2, 1)), ((5, 4, 3, 2), (1)))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_of_alternates(()), ((), ()))
        self.assertEqual(sum_of_alternates((0, 0)), ((0), (0)))
        self.assertEqual(sum_of_alternates((1000000000000000000,)), ((1000000000000000000,)))

    def test_complex_scenarios(self):
        self.assertEqual(sum_of_alternates((1, 2, 0, 3, 0, 4, 0, 5)), ((1, 2, 3, 4), (0, 0, 0, 5)))
        self.assertEqual(sum_of_alternates((0, 1, 0, 2, 0, 3, 0, 4, 0, 5)), ((0, 1, 0, 2, 0, 3, 0, 4), (5)))
