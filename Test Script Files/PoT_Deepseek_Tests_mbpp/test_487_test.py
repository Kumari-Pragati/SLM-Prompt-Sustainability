import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_tuple(((1, 2), (3, 4), (5, 6))), 
                         ((1, 2), (3, 4), (5, 6)))

    def test_edge_case_single_element(self):
        self.assertEqual(sort_tuple(((1, 2))), 
                         ((1, 2)))

    def test_boundary_case_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_corner_case_same_last_elements(self):
        self.assertEqual(sort_tuple(((1, 2), (1, 3))), 
                         ((1, 2), (1, 3)))

    def test_tricky_case_reverse_order(self):
        self.assertEqual(sort_tuple(((2, 3), (1, 2))), 
                         ((1, 2), (2, 3)))
