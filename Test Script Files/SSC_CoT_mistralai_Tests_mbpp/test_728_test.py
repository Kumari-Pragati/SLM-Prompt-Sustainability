import unittest
from mbpp_728_code import sum_list

class TestSumList(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(sum_list([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEqual(sum_list([0, 0, 0], [1, 2, 3]), [1, 2, 4])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sum_list([], []), [])
        self.assertEqual(sum_list([1], []), [1])
        self.assertEqual(sum_list([1, 2], []), [1, 2])
        self.assertEqual(sum_list([], [1]), [])
        self.assertEqual(sum_list([], [1, 2]), [])

    def test_negative_numbers(self):
        self.assertEqual(sum_list([-1, -2, -3], [-4, -5, -6]), [-5, -7, -9])
        self.assertEqual(sum_list([0, -1, -2], [1, -3, -4]), [1, -1, -5])

    def test_mixed_types(self):
        self.assertRaises(TypeError, sum_list, [1, 2, 3], [4, "5", 6])
        self.assertRaises(TypeError, sum_list, [1, 2, 3], [4, 5, "6"])
