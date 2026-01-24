import unittest
from mbpp_949_code import sort_list

class TestSortList(unittest.TestCase):

    def test_sort_list_normal(self):
        self.assertEqual(sort_list([1, 10, 100, 2, 20]), "'[1, 2, 10, 20, 100]'")
        self.assertEqual(sort_list(['a', 'aa', 'aaa', 'b', 'bb']), "'['aa', 'aaa', 'b', 'a', 'bb']'")

    def test_sort_list_edge_cases(self):
        self.assertEqual(sort_list([0, 0.001, 0.0001]), "'[0, 0.0001, 0.001]'")
        self.assertEqual(sort_list([-1, -10, -100, -2, -20]), "'[-20, -2, -100, -10, -1]'")
        self.assertEqual(sort_list([1.1, 1.001, 1.0001]), "'[1.0001, 1.001, 1.1]'")
        self.assertEqual(sort_list([-1.1, -1.001, -1.0001]), "'[-1.0001, -1.001, -1.1]'")

    def test_sort_list_empty_list(self):
        self.assertEqual(sort_list([]), "'[]'")

    def test_sort_list_mixed_types(self):
        self.assertRaises(TypeError, sort_list, [1, 'a', 3.14])
