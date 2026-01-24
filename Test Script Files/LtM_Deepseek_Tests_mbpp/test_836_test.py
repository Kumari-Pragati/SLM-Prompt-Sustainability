import unittest
from mbpp_836_code import max_sub_array_sum

class TestMaxSubArraySum(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)
        self.assertEqual(max_sub_array_sum([1, -2, 3, -4], 4), 3)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(max_sub_array_sum([], 0), 0)
        self.assertEqual(max_sub_array_sum([-1], 1), 1)
        self.assertEqual(max_sub_array_sum([1], 1), 1)
        self.assertEqual(max_sub_array_sum([0], 1), 1)

    # Test for more complex or corner cases
    def test_complex_cases(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)
        self.assertEqual(max_sub_array_sum([-1, -2, -3, -4], 4), 1)
        self.assertEqual(max_sub_array_sum([1, 2, 3, 4], 4), 4)
        self.assertEqual(max_sub_array_sum([0, 0, 0, 0], 4), 1)
