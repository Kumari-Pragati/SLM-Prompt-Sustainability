import unittest
from mbpp_915_code import rearrange_numbs

class TestRearrangeNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(rearrange_numbs([1, 2, 3, 4, 0]), [0, 1, 1/2, 1/3, 1/4])
        self.assertEqual(rearrange_numbs([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_edge_conditions(self):
        self.assertEqual(rearrange_numbs([0]), [0])
        self.assertEqual(rearrange_numbs([]), [])

    def test_boundary_conditions(self):
        self.assertEqual(rearrange_numbs([1]), [1])
        self.assertEqual(rearrange_numbs([-1]), [-1])
        self.assertEqual(rearrange_numbs([float('inf')]), [float('inf')])
        self.assertEqual(rearrange_numbs([float('-inf')]), [float('-inf')])

    def test_complex_cases(self):
        self.assertEqual(rearrange_numbs([2, 3, 4, 5]), [1/5, 1/4, 1/3, 1/2])
        self.assertEqual(rearrange_numbs([0, 1, 2, 3]), [0, 1, 1/2, 1/3])
        self.assertEqual(rearrange_numbs([1, 2, 0, 3]), [0, 1, 1/2, 1/3])
