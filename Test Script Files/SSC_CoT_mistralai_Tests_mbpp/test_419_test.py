import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(round_and_sum([1.1, 2.2, 3.3]), 16)
        self.assertEqual(round_and_sum([-1.1, -2.2, -3.3]), 16)

    def test_edge_cases(self):
        self.assertEqual(round_and_sum([0.0]), 0)
        self.assertEqual(round_and_sum([0.1, 0.2, 0.3]), 3)
        self.assertEqual(round_and_sum([1000.1, 2000.2, 3000.3]), 18000000)

    def test_boundary_cases(self):
        self.assertEqual(round_and_sum([-1e-5, 1e-5]), 2)
        self.assertEqual(round_and_sum([-1e5, 1e5]), 2000000)

    def test_special_cases(self):
        self.assertEqual(round_and_sum([0.0, 0.0]), 0)
        self.assertEqual(round_and_sum([1.1, -1.1]), 0)
        self.assertEqual(round_and_sum([1.1, 1.1]), 2)
