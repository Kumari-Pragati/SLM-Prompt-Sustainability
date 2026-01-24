import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 30)
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), 30)
        self.assertEqual(round_and_sum([0.0, 0.0, 0.0]), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(round_and_sum([float('inf')]), float('inf'))
        self.assertEqual(round_and_sum([float('-inf')]), float('-inf'))
        self.assertEqual(round_and_sum([-1e308, 0, 1e308]), 2 * 1e308)
        self.assertEqual(round_and_sum([-1e-308, 0, 1e-308]), 2 * 1e-308)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0]), 9)
        self.assertEqual(round_and_sum([-1.0, -2.0, -3.0]), 9)

    def test_complex_scenarios(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, 4.4]), 30)
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3, -4.4]), 30)
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5]), 30)
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3, -4.4, -5.5]), 30)
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3, 4.4, 5.5, 6.6]), 36)
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3, -4.4, -5.5, -6.6]), 36)
