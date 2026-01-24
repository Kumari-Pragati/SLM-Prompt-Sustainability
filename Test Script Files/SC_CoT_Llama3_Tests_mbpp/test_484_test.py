import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):
    def test_typical_case(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 1), (4, 3)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case_empty_list1(self):
        test_list1 = []
        test_list2 = [(2, 1), (4, 3)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [])

    def test_edge_case_empty_list2(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = []
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), test_list1)

    def test_edge_case_list1_subset_list2(self):
        test_list1 = [(2, 1), (4, 3)]
        test_list2 = [(1, 2), (3, 4), (5, 6)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [])

    def test_edge_case_list2_subset_list1(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 1)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [(1, 2), (3, 4), (5, 6)])

    def test_edge_case_list1_subset_list2_subset_list1(self):
        test_list1 = [(2, 1), (4, 3)]
        test_list2 = [(1, 2), (3, 4)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [])

    def test_edge_case_list2_subset_list1_subset_list2(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = [(2, 1), (4, 3)]
        self.assertEqual(remove_matching_tuple(test_list1, test_list2), [(1, 2), (3, 4), (5, 6)])

    def test_invalid_input_non_list1(self):
        test_list1 = 'not a list'
        test_list2 = [(2, 1), (4, 3)]
        with self.assertRaises(TypeError):
            remove_matching_tuple(test_list1, test_list2)

    def test_invalid_input_non_list2(self):
        test_list1 = [(1, 2), (3, 4), (5, 6)]
        test_list2 = 'not a list'
        with self.assertRaises(TypeError):
            remove_matching_tuple(test_list1, test_list2)

    def test_invalid_input_mixed_type(self):
        test_list1 = [(1, 2), 'not a tuple', (3, 4), (5, 6)]
        test_list2 = [(2, 1), (4, 3)]
        with self.assertRaises(TypeError):
            remove_matching_tuple(test_list1, test_list2)
