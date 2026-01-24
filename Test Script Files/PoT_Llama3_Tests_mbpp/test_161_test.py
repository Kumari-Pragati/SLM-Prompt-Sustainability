import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2, 4]), [1, 3, 5])

    def test_edge_case_empty_list1(self):
        self.assertEqual(remove_elements([], [2, 4]), [])

    def test_edge_case_empty_list2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], []), [1, 2, 3, 4, 5])

    def test_edge_case_list1_subset_of_list2(self):
        self.assertEqual(remove_elements([1, 2, 3], [1, 2, 3, 4, 5]), [])

    def test_edge_case_list1_superset_of_list2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2]), [3, 4, 5])

    def test_edge_case_list1_and_list2_empty(self):
        self.assertEqual(remove_elements([], []), [])

    def test_edge_case_list1_and_list2_same(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), [])

    def test_edge_case_list1_and_list2_duplicates(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 5], [2, 4]), [1, 3, 5])

    def test_edge_case_list1_and_list2_duplicates_in_list1(self):
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 5], [2, 2, 4]), [1, 3, 5])

    def test_edge_case_list1_and_list2_duplicates_in_list2(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5], [2, 2, 4]), [1, 3, 5])
