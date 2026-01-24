import unittest
from mbpp_265_code import list_split

class TestListSplit(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), 
                         [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])

    def test_edge_case(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 
                         [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

    def test_boundary_case(self):
        self.assertEqual(list_split([], 2), [])

    def test_special_case(self):
        self.assertEqual(list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), 
                         [[1, 4, 7, 10], [2, 5, 8], [3, 6, 9]])

    def test_invalid_step(self):
        with self.assertRaises(IndexError):
            list_split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
