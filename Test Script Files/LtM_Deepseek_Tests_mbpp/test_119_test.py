import unittest
from mbpp_119_code import search

class TestSearchFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(search([1, 2, 3, 4], 4), 8)

    def test_edge_condition_empty_input(self):
        self.assertEqual(search([], 0), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(search([5], 1), 5)

    def test_boundary_condition_max_value(self):
        self.assertEqual(search([2**31 - 1, 2**31 - 1], 2), 2**31 - 1)

    def test_boundary_condition_min_value(self):
        self.assertEqual(search([0, 0], 2), 0)

    def test_complex_case_duplicate_elements(self):
        self.assertEqual(search([1, 2, 1, 2], 4), 0)

    def test_complex_case_negative_elements(self):
        self.assertEqual(search([-1, -2, -3, -4], 4), -8)
