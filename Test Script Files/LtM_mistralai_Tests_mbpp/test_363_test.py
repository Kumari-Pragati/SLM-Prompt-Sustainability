import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(add_K_element([(1, 2), (3, 4)], 1), [(2, 3), (4, 5)])
        self.assertListEqual(add_K_element([(0, 0), (1, 1)], 2), [(2, 2), (3, 3)])

    def test_edge_cases(self):
        self.assertListEqual(add_K_element([], 1), [])
        self.assertListEqual(add_K_element([(0, 0)], 0), [(0, 0)])
        self.assertListEqual(add_K_element([(1, 2), (3, 4)], 0), [(1, 2), (3, 4)])

    def test_negative_k(self):
        self.assertListEqual(add_K_element([(1, 2), (3, 4)], -1), [(0, 1), (2, 3)])

    def test_large_input(self):
        large_list = [(i, i * 2) for i in range(10)]
        self.assertListEqual(add_K_element(large_list, 5), [(5, 10), (6, 12), (7, 14), (8, 16), (9, 18)])
