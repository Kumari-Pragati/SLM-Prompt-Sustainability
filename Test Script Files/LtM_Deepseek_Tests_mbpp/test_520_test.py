import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_lcm([2, 7]), 14)
        self.assertEqual(get_lcm([3, 5]), 15)
        self.assertEqual(get_lcm([10, 20]), 20)

    def test_edge_conditions(self):
        self.assertEqual(get_lcm([0, 5]), 0)
        self.assertEqual(get_lcm([-2, 7]), -14)
        self.assertEqual(get_lcm([2, 0]), 0)
        self.assertEqual(get_lcm([-2, 0]), 0)

    def test_complex_cases(self):
        self.assertEqual(get_lcm([12, 15, 21]), 420)
        self.assertEqual(get_lcm([100, 200, 300]), 6000)
        self.assertEqual(get_lcm([1000, 2000, 3000]), 6000000)
