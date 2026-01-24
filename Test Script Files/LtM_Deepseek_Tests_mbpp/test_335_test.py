import unittest
from mbpp_335_code import ap_sum

class TestAPSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(ap_sum(1, 5, 2), 14)
        self.assertEqual(ap_sum(10, 10, 1), 100)

    def test_edge_conditions(self):
        self.assertEqual(ap_sum(0, 0, 0), 0)
        self.assertEqual(ap_sum(1, 1, 1), 1)
        self.assertEqual(ap_sum(100, 1, 0), 100)

    def test_boundary_conditions(self):
        self.assertEqual(ap_sum(1, 1000, 1), 500500)
        self.assertEqual(ap_sum(1, 1000, -1), 500500)
        self.assertEqual(ap_sum(-1, 1000, 1), -500500)
        self.assertEqual(ap_sum(-1, 1000, -1), -500500)

    def test_complex_cases(self):
        self.assertEqual(ap_sum(100, 10, -2), 900)
        self.assertEqual(ap_sum(-100, 10, 2), -900)
        self.assertEqual(ap_sum(-100, 10, -2), -900)
