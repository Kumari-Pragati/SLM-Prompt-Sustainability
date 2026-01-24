import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5]), [1, 2, 4, 5])
        self.assertEqual(replace_list(['a', 'b', 'c'], ['d', 'e']), ['a', 'b', 'd', 'e'])

    def test_edge_case_empty_list1(self):
        self.assertEqual(replace_list([], [4, 5]), [4, 5])

    def test_edge_case_empty_list2(self):
        self.assertEqual(replace_list([1], []), [1])

    def test_corner_case_single_element_list1(self):
        self.assertEqual(replace_list([1], [2]), [2])

    def test_corner_case_single_element_list2(self):
        self.assertEqual(replace_list([1], [2, 3]), [2, 3])
