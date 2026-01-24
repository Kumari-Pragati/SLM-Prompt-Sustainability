import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(nth_nums([1, 2, 3], 2), [1, 4, 9])
        self.assertEqual(nth_nums([4, 5, 6], 3), [64, 125, 216])

    def test_edge_conditions(self):
        self.assertEqual(nth_nums([0], 1), [0])
        self.assertEqual(nth_nums([0], 0), [1])
        self.assertEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])

    def test_boundary_conditions(self):
        self.assertEqual(nth_nums([10000], 1000), [10**2000])
        self.assertEqual(nth_nums([-10000], 1000), [10**2000])

    def test_complex_cases(self):
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], 0), [1, 1, 1, 1, 1])
        self.assertEqual(nth_nums([1, 2, 3, 4, 5], -1), [1, 1, 1, 1, 1])
