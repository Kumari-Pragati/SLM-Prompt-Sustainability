import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_tuple(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'), (5, 'e'))), 
                         ((1, 'a'), (2, 'b'), (5, 'e')))
        self.assertEqual(sort_tuple(((1, 'a'), (1, 'b'), (1, 'c'))), 
                         ((1, 'a'), (1, 'b'), (1, 'c')))
        self.assertEqual(sort_tuple(((0, 'z'), (-1, 'y'), (-2, 'x'))), 
                         ((-2, 'x'), (-1, 'y'), (0, 'z')))
        self.assertEqual(sort_tuple(((10, 'j'), (9, 'i'), (8, 'h'))), 
                         ((8, 'h'), (9, 'i'), (10, 'j')))
