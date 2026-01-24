import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)
        self.assertEqual(count_range_in_list([-5, -4, -3, -2, -1], -3, -1), 4)
        self.assertEqual(count_range_in_list([0, 0, 1, 0, 0], 0, 1), 2)

    def test_edge_cases(self):
        self.assertEqual(count_range_in_list([1, 2, 3], 1, 3), 3)
        self.assertEqual(count_range_in_list([1, 2, 3], 1, 4), 3)
        self.assertEqual(count_range_in_list([1, 2, 3], 0, 3), 3)
        self.assertEqual(count_range_in_list([1, 2, 3], -1, 3), 0)
        self.assertEqual(count_range_in_list([1, 2, 3], 1, -1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_range_in_list([-1, 0, 1], -1, 1), 2)
        self.assertEqual(count_range_in_list([-1, 0, 1], -1, 0), 1)
        self.assertEqual(count_range_in_list([-1, 0, 1], 0, 1), 2)
        self.assertEqual(count_range_in_list([-1, 0, 1], 0, 0), 1)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_range_in_list, [1, 2, 3], 'a', 4)
        self.assertRaises(TypeError, count_range_in_list, [1, 2, 3], 1, 'a')
        self.assertRaises(TypeError, count_range_in_list, [1, 2, 3], 1, None)
        self.assertRaises(TypeError, count_range_in_list, [1, 2, 3], 1, (1, 2, 3))
