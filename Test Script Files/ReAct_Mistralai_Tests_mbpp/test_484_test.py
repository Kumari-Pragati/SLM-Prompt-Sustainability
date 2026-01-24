import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(remove_matching_tuple([], []), [])

    def test_single_element_lists(self):
        self.assertListEqual(remove_matching_tuple([(1, 2)], []), [(1, 2)])
        self.assertListEqual(remove_matchingTuple([], [(1, 2)]), [])

    def test_matching_elements(self):
        self.assertListEqual(remove_matchingTuple([(1, 2), (3, 4), (1, 2)], [(1, 2)]), [(3, 4)])

    def test_no_matching_elements(self):
        self.assertListEqual(remove_matchingTuple([(1, 2), (3, 4)], [(5, 6)]), [(1, 2), (3, 4)])

    def test_mixed_data_types(self):
        self.assertRaises(TypeError, remove_matchingTuple, [1, 2, (3, 4)], [1, 2, 3])

    def test_list_with_none(self):
        self.assertListEqual(remove_matchingTuple([None, (1, 2)], [None, (1, 2)]), [])

    def test_list_with_duplicates(self):
        self.assertListEqual(remove_matchingTuple([(1, 2), (1, 2)], [(1, 2)]), [])
