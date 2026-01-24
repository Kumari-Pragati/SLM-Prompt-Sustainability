import unittest
from mbpp_301_code import dict_depth

class TestDictDepth(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}), 3)
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': 2}}), 2)
        self.assertEqual(dict_depth({'a': 1}), 1)
        self.assertEqual(dict_depth({}), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1}}}}}}}), 6)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1, 'h': 2}}}}}}}), 7)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1, 'h': 2, 'i': [1, 2, 3]}}}}}}}), 8)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1, 'h': 2, 'i': [1, 2, 3, 4]}}}}}}}), 9)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1, 'h': 2, 'i': [1, 2, 3, 4, 5, 6, 7, 8, 9]}}}}}}}), 10)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1, 'h': 2, 'i': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100}}}}}}}), 101)
        self.assertEqual(dict_depth({'a': {'b': {'c': {'d': {'e': {'f': {'g': 1, 'h': 2, 'i': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26