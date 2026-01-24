import unittest
from mbpp_333_code import Sort

class TestSortFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Sort([(1, 2), (3, 1), (2, 3)]), [(3, 1), (2, 3), (1, 2)])

    def test_edge_case_empty_list(self):
        self.assertEqual(Sort([]), [])

    def test_boundary_case_single_element(self):
        self.assertEqual(Sort([(1, 2)]), [(1, 2)])

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(Sort([(1, 2), (1, 2)]), [(1, 2), (1, 2)])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            Sort("not a list")

    def test_invalid_tuple_elements(self):
        with self.assertRaises(TypeError):
            Sort([1, 2, 3])
