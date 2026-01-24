import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(sort_list_last([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]), [(4, 'd'), (3, 'c'), (2, 'b'), (1, 'a')])
        self.assertEqual(sort_list_last([('z', 1), ('y', 2), ('x', 3), ('w', 4)]), [('w', 4), ('x', 3), ('y', 2), ('z', 1)])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(sort_list_last([(1, 'a'), (1, 'b'), (1, 'c')]), [(1, 'c'), (1, 'b'), (1, 'a')])
        self.assertEqual(sort_list_last([('z', 1), ('y', 1), ('x', 1)]), [('z', 1), ('y', 1), ('x', 1)])
        self.assertEqual(sort_list_last([(1, 'a'), (1, 1), (1, 'c')]), [(1, 'c'), (1, 1), (1, 'a')])
        self.assertEqual(sort_list_last([('z', 1), ('y', 1), (1, 1)]), [('z', 1), ('y', 1), (1, 1)])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, sort_list_last, [1, 2, 3])
        self.assertRaises(TypeError, sort_list_last, [(1,), (2,)])
