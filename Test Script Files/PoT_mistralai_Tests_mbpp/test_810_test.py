import unittest
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])

    def test_edge_case_single_element(self):
        self.assertListEqual(count_variable(5, 0, 0, 0), [5])

    def test_edge_case_no_elements(self):
        self.assertListEqual(count_variable(0, 0, 0, 0), [])

    def test_edge_case_single_pair(self):
        self.assertListEqual(count_variable(1, 2, 0, 0), [1, 2])

    def test_edge_case_multiple_pairs(self):
        self.assertListEqual(count_variable(1, 2, 3, 4), [1, 2, 3, 4])

    def test_corner_case_duplicate_elements(self):
        self.assertListEqual(count_variable(1, 1, 1, 1), [1, 1])
