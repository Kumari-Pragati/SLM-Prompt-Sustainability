import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4], 5), 4)

    def test_edge_case_empty_arrays(self):
        self.assertEqual(find_Extra([], [], 0), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_corner_case_extra_element_at_start(self):
        self.assertEqual(find_Extra([2, 1, 2, 2, 2], [1, 2, 2, 2], 5), 0)

    def test_corner_case_extra_element_at_end(self):
        self.assertEqual(find_Extra([1, 2, 2, 2, 3], [1, 2, 2, 2], 5), 4)

    def test_corner_case_extra_element_in_middle(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 4, 5], 5), 2)
