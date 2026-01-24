import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    
    def test_typical_case(self):
        list = [[1, 5, 8], [4, 12], [7, 8, 10, 12]]
        self.assertEqual(find_minimum_range(list), (4, 5))

    def test_edge_case_single_list(self):
        list = [[1, 5, 8]]
        self.assertEqual(find_minimum_range(list), (1, 8))

    def test_edge_case_empty_lists(self):
        list = [[], [], []]
        self.assertRaises(Exception, find_minimum_range, list)

    def test_edge_case_empty_list(self):
        list = []
        self.assertRaises(Exception, find_minimum_range, list)

    def test_corner_case_duplicate_values(self):
        list = [[1, 5, 8], [4, 12], [7, 8, 10, 12]]
        self.assertEqual(find_minimum_range(list), (4, 5))

    def test_invalid_input_non_list(self):
        self.assertRaises(TypeError, find_minimum_range, 123)

    def test_invalid_input_list_of_non_list(self):
        self.assertRaises(TypeError, find_minimum_range, [1, 2, 3])
