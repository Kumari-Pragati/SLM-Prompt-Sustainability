import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(min_Ops([1, 1, 1], 3, 2), 1)
        self.assertEqual(min_Ops([10, 10, 10], 3, 5), 2)

    def test_edge_conditions(self):
        self.assertEqual(min_Ops([], 0, 5), -1)
        self.assertEqual(min_Ops([1, 2, 3], 3, 0), -1)
        self.assertEqual(min_Ops([1, 2, 3], 3, 1), 0)

    def test_complex_cases(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 5)
        self.assertEqual(min_Ops([10, 20, 30, 40, 50], 5, 10), 5)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 3), -1)
