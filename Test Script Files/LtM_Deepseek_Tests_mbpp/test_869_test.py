import unittest
from mbpp_869_code import remove_list_range

class TestRemoveListRange(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 1, 4), [[1, 2], [3, 4]])

    def test_edge_conditions(self):
        self.assertEqual(remove_list_range([], 1, 4), [])
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 5, 6), [])
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 1, 1), [[1, 2]])
        self.assertEqual(remove_list_range([[1, 2], [3, 4]], 2, 3), [[1, 2]])

    def test_complex_cases(self):
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 2, 5), [[2, 3], [4, 5]])
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 1, 6), [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(remove_list_range([[1, 2], [3, 4], [5, 6]], 3, 4), [[3, 4]])
