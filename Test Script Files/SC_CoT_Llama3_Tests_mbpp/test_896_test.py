import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(sort_list_last([(1,2,3), (4,5,6), (7,8,9)]), [(1,2,3), (4,5,6), (7,8,9)])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(sort_list_last([(1,2,3)]), [(1,2,3)])

    def test_edge_case_all_equal_elements(self):
        self.assertEqual(sort_list_last([(1,1,1), (2,2,2), (3,3,3)]), [(1,1,1), (2,2,2), (3,3,3)])

    def test_edge_case_all_elements_equal(self):
        self.assertEqual(sort_list_last([(1,1,1), (1,1,1), (1,1,1)]), [(1,1,1), (1,1,1), (1,1,1)])

    def test_edge_case_negative_numbers(self):
        self.assertEqual(sort_list_last([(-1,-2,-3), (-4,-5,-6), (-7,-8,-9)]), [(-1,-2,-3), (-4,-5,-6), (-7,-8,-9)])

    def test_edge_case_mixed_negative_and_positive_numbers(self):
        self.assertEqual(sort_list_last([(-1,-2,-3), (4,5,6), (-7,-8,-9)]), [(-1,-2,-3), (-7,-8,-9), (4,5,6)])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            sort_list_last("invalid input")
