import unittest
from mbpp_75_code import find_tuples

class TestFindTuples(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(find_tuples([[10, 20], [20, 30], [40, 50]], 10), ['[10, 20]', '[20, 30]'])
        self.assertListEqual(find_tuples([[100, 200], [200, 300], [400, 500]], 100), ['[100, 200]', '[200, 300]'])

    def test_edge_case_empty_list(self):
        self.assertListEqual(find_tuples([], 10), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(find_tuples([[10]], 10), ['[10]'])

    def test_edge_case_single_element_not_multiple(self):
        self.assertListEqual(find_tuples([[11]], 10), [])

    def test_edge_case_single_element_zero(self):
        self.assertListEqual(find_tuples([[0]], 10), [])

    def test_edge_case_negative_numbers(self):
        self.assertListEqual(find_tuples([[-10, -20], [-20, -30], [-40, -50]], 10), [])

    def test_corner_case_mixed_numbers(self):
        self.assertListEqual(find_tuples([[10, 20, 30], [40, 50]], 10), ['[10, 20]', ''])
