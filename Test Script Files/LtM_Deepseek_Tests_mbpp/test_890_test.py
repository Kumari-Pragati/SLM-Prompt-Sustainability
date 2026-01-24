import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4], 5), 4)

    def test_edge_case_empty_arrays(self):
        self.assertEqual(find_Extra([], [], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)

    def test_boundary_case_maximum_values(self):
        self.assertEqual(find_Extra([1000000000]*10, [1000000000]*9 + [1], 10), 9)

    def test_complex_case_duplicate_elements(self):
        self.assertEqual(find_Extra([1, 2, 2, 3, 4, 5], [1, 2, 3, 4, 5], 6), 2)

    def test_complex_case_elements_out_of_order(self):
        self.assertEqual(find_Extra([1, 3, 2, 4, 5], [1, 2, 3, 4, 5], 5), 0)
