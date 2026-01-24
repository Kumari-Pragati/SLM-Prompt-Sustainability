import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_sublists([1]), [1])

    def test_two_element_lists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])
        self.assertEqual(sort_sublists([[3, 4], [1, 2]]), [[1, 2], [3, 4]])

    def test_multiple_element_lists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6], [7, 8]]),
                         [[1, 2], [3, 4], [5, 6], [7, 8]])
        self.assertEqual(sort_sublists([[7, 8], [5, 6], [3, 4], [1, 2]]),
                         [[1, 2], [3, 4], [5, 6], [7, 8]])
