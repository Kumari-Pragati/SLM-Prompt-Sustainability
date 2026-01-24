import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'), (3, 'c'))), 
                         ((1, 'a'), (2, 'b'), (3, 'c')))

    def test_edge_case(self):
        self.assertEqual(sort_tuple(((1, 'a'),)), ((1, 'a'),))

    def test_boundary_case(self):
        self.assertEqual(sort_tuple(()), ())

    def test_corner_case(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'), (1, 'b'), (2, 'a'))), 
                         ((1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')))
