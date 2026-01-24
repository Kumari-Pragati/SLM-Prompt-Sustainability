import unittest
from mbpp_154_code import specified_element

class TestSpecifiedElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(specified_element([[1, 2], [3, 4]], 0), [1, 3])
        self.assertListEqual(specified_element([[1, 2], [3, 4]], 1), [2, 4])

    def test_edge_case_empty_list(self):
        self.assertListEqual(specified_element([], 0), [])

    def test_edge_case_empty_sublist(self):
        self.assertListEqual(specified_element([[1], []], 0), [1])
        self.assertListEqual(specified_element([[1], []], 1), [])

    def test_edge_case_negative_index(self):
        self.assertListEqual(specified_element([[1], [2]], -1), [])

    def test_edge_case_out_of_range_index(self):
        self.assertListEqual(specified_element([[1], [2]], 2), [])
