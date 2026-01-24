import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5]), [1, 2, 4, 5])
        self.assertEqual(replace_list(['a', 'b', 'c'], ['d', 'e']), ['a', 'b', 'd', 'e'])

    def test_edge_cases(self):
        self.assertEqual(replace_list([], [1]), [1])
        self.assertEqual(replace_list([1], []), [1])
        self.assertEqual(replace_list([1], [1]), [1])
        self.assertEqual(replace_list([1, 2], [3]), [1, 2, 3])
        self.assertEqual(replace_list([1, 2], [1, 3]), [1, 2, 3])

    def test_boundary_conditions(self):
        self.assertEqual(replace_list([1, 2, 3, 4], [5]), [1, 2, 3, 5])
        self.assertEqual(replace_list([1, 2, 3, 4], [1, 5]), [1, 2, 3, 5])
        self.assertEqual(replace_list([1, 2, 3, 4], [5, 1]), [5, 2, 3, 4])
        self.assertEqual(replace_list([1, 2, 3, 4], [1, 5, 2]), [1, 5, 2, 3, 4])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, replace_list, 1, 2)
        self.assertRaises(TypeError, replace_list, [1], 2)
        self.assertRaises(TypeError, replace_list, 1, [2])
