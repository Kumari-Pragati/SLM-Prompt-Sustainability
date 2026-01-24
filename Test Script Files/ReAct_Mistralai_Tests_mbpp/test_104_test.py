import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_sort_sublists_single_element_list(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[[1, 2]]])
        self.assertEqual(sort_sublists([[2, 1]]), [[[2, 1]]])

    def test_sort_sublists_multiple_elements_same_key(self):
        self.assertEqual(sort_sublists([[[1, 2], [1, 3]], [[2, 1], [2, 3]]]),
                         [[[[1, 2], [1, 3]], [[2, 1], [2, 3]]],
                          [[[1, 2], [1, 3]], [[2, 1], [2, 3]]]])

    def test_sort_sublists_multiple_elements_different_keys(self):
        self.assertEqual(sort_sublists([[[2, 1], [1, 2]], [[3, 2], [2, 3]]]),
                         [[[[2, 1], [1, 2]], [[3, 2], [2, 3]]],
                          [[[1, 2], [2, 1]], [[2, 3], [3, 2]]]])

    def test_sort_sublists_mixed_types(self):
        self.assertRaises(TypeError, sort_sublists, [[1, 2], 'a', [3, 4]])

    def test_sort_sublists_negative_numbers(self):
        self.assertEqual(sort_sublists([[-2, -1], [-1, -2], [1, 2]]),
                         [[[-2, -1], [-1, -2]], [ [1, 2]]])
