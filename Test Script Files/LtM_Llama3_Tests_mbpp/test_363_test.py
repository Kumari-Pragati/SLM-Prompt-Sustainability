import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(add_K_element([[1, 2], [3, 4]], 1), [[2, 3], [4, 5]])

    def test_empty_input(self):
        self.assertEqual(add_K_element([], 1), [])

    def test_single_element_input(self):
        self.assertEqual(add_K_element([[1]], 1), [[2]])

    def test_negative_K(self):
        self.assertEqual(add_K_element([[1, 2], [3, 4]], -1), [[0, 1], [2, 3]])

    def test_K_as_zero(self):
        self.assertEqual(add_K_element([[1, 2], [3, 4]], 0), [[1, 2], [3, 4]])

    def test_K_as_large_number(self):
        self.assertEqual(add_K_element([[1, 2], [3, 4]], 100), [[101, 102], [103, 104]])

    def test_list_of_lists_with_differing_lengths(self):
        self.assertEqual(add_K_element([[1, 2, 3], [4, 5]], 1), [[2, 3, 4], [5, 6]])
