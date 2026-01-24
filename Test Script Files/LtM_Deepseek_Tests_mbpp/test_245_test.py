import unittest
from mbpp_245_code import max_sum

class TestMaxSum(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(max_sum([1, 2, 3, 4], 4), 10)
        self.assertEqual(max_sum([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum([5, 4, 3, 2, 1], 5), 15)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(max_sum([], 0), float("-inf"))
        self.assertEqual(max_sum([1], 1), 1)
        self.assertEqual(max_sum([-1, -2, -3, -4], 4), -1)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 6], 6), 21)
        self.assertEqual(max_sum([1, 2, 3, 4, 5, 0], 6), 15)
        self.assertEqual(max_sum([1, 2, 3, 4, 0, 5], 6), 15)
        self.assertEqual(max_sum([1, 2, 3, 0, 4, 5], 6), 15)
        self.assertEqual(max_sum([0, 0, 0, 0, 0, 0], 6), 0)
