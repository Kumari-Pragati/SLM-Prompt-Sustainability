import unittest
from mbpp_342_code import find_minimum_range

class TestFindMinimumRange(unittest.TestCase):

    def test_typical_case(self):
        list = [[1, 2, 3], [0, 8, 9], [5, 6, 7]]
        self.assertEqual(find_minimum_range(list), (0, 1))

    def test_edge_case_single_list(self):
        list = [[1, 2, 3]]
        self.assertEqual(find_minimum_range(list), (1, 3))

    def test_edge_case_empty_list(self):
        list = []
        with self.assertRaises(ValueError):
            find_minimum_range(list)

    def test_edge_case_single_element_in_list(self):
        list = [[1]]
        self.assertEqual(find_minimum_range(list), (1, 1))

    def test_explicitly_handled_error_case(self):
        list = [None, [1, 2, 3]]
        with self.assertRaises(TypeError):
            find_minimum_range(list)
