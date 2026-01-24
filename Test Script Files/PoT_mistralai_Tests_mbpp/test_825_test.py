import unittest
from mbpp_825_code import access_elements

class TestAccessElements(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(access_elements([1, 2, 3, 4, 5], [1, 3]), [1, 3])

    def test_edge_case_empty_list(self):
        self.assertListEqual(access_elements([], [0]), [])

    def test_edge_case_empty_index(self):
        self.assertListEqual(access_elements([1, 2, 3], []), [])

    def test_edge_case_negative_index(self):
        self.assertListEqual(access_elements([1, 2, 3], [-1]), [3])

    def test_edge_case_out_of_bounds_index(self):
        self.assertListEqual(access_elements([1, 2, 3], [3, 4]), [])

    def test_corner_case_negative_index_out_of_bounds(self):
        self.assertListEqual(access_elements([1, 2, 3], [-5]), [])
