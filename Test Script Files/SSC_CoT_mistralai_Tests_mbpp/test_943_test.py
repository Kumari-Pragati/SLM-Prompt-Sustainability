import unittest
from mbpp_943_code import combine_lists

class TestCombineLists(unittest.TestCase):

    def test_normal_operation(self):
        self.assertListEqual(combine_lists([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertListEqual(combine_lists([], [1, 2, 3]), [1, 2, 3])
        self.assertListEqual(combine_lists([1, 2, 3], []), [1, 2, 3])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(combine_lists([0, 0, 0], [1, 2, 3]), [0, 0, 0, 1, 2, 3])
        self.assertListEqual(combine_lists([1, 2, 3], [0, 0, 0]), [1, 2, 3, 0, 0, 0])
        self.assertListEqual(combine_lists([-1, -2, -3], [1, 2, 3]), [-1, -2, -3, 1, 2, 3])
        self.assertListEqual(combine_lists([1, 2, 3], [-1, -2, -3]), [1, 2, 3, -1, -2, -3])

    def test_invalid_inputs(self):
        # If the function does not handle invalid inputs, this block can be omitted.
        with self.assertRaises(TypeError):
            combine_lists('1', '2')
        with self.assertRaises(TypeError):
            combine_lists([1], '2')
        with self.assertRaises(TypeError):
            combine_lists('1', [2])
