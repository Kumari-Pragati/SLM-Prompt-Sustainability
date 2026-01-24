import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3)]), 
                         [(2, 3), (1, 2), (4, 4), (2, 5)])

    def test_edge_case_single_element(self):
        self.assertEqual(sort_list_last([(2, 1)]), [(2, 1)])

    def test_boundary_case_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_corner_case_duplicate_last_elements(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 5), (4, 4), (2, 4)]), 
                         [(2, 4), (1, 5), (4, 4), (2, 5)])
