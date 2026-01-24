import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(search([1, 2, 3, 2, 1], 5), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(search([5], 1), 5)

    def test_boundary_case_empty_array(self):
        self.assertEqual(search([], 0), 0)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(search([1, 1, 2, 2, 3, 3], 6), 0)

    def test_tricky_case_large_array(self):
        self.assertEqual(search(list(range(1, 10001)), 10000), 5000)
