import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):
    def test_typical_input(self):
        list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(find_minimum_range(list), (1, 9))

    def test_edge_case(self):
        list = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(find_minimum_range(list), (1, 6))

    def test_edge_case2(self):
        list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(find_minimum_range(list), (1, 12))

    def test_empty_list(self):
        list = []
        with self.assertRaises(IndexError):
            find_minimum_range(list)

    def test_single_element_list(self):
        list = [[1]]
        self.assertEqual(find_minimum_range(list), (1, 1))

    def test_single_element_list2(self):
        list = [[1, 2]]
        self.assertEqual(find_minimum_range(list), (1, 2))

    def test_single_element_list3(self):
        list = [[1, 2, 3, 4, 5]]
        self.assertEqual(find_minimum_range(list), (1, 5))
