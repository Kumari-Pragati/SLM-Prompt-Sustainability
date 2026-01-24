import unittest
from mbpp_780_code import find_combinations

class TestFindCombinations(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_combinations([(1, 2), (3, 4)]), [(4, 6), (5, 6), (7, 8)])

    def test_edge_case_empty_list(self):
        self.assertEqual(find_combinations([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(find_combinations([(1, 2)]), [])

    def test_edge_case_two_element_list(self):
        self.assertEqual(find_combinations([(1, 2), (3, 4)]), [(4, 6)])

    def test_edge_case_duplicates(self):
        self.assertEqual(find_combinations([(1, 1), (2, 2)]), [])

    def test_edge_case_non_integer_values(self):
        self.assertEqual(find_combinations([("a", "b"), ("c", "d")]), [('b', 'd'), ('c', 'd')])

    def test_edge_case_non_list_input(self):
        with self.assertRaises(TypeError):
            find_combinations("not a list")
