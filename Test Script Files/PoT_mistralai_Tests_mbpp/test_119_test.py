import unittest
from mbpp_119_code import search

class TestSearch(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(search([10, 20, 30, 40, 50], 5), 15)

    def test_edge_case_empty_list(self):
        self.assertEqual(search([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(search([1], 1), 1)

    def test_edge_case_single_bit_flip(self):
        self.assertEqual(search([1, 2, 3, 4, 5], 4), 1)

    def test_edge_case_all_bits_set(self):
        self.assertEqual(search([2**i for i in range(5)], 5), 31)

    def test_edge_case_all_bits_unset(self):
        self.assertEqual(search([0] * 5, 5), 0)
