import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_edge_case_duplicates_at_start(self):
        self.assertEqual(remove_duplicate([2, 2, 3]), [2, 3])

    def test_edge_case_duplicates_at_end(self):
        self.assertEqual(remove_duplicate([1, 1, 3]), [1, 3])

    def test_edge_case_duplicates_in_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3]), [1, 2, 3])

    def test_corner_case_duplicates_only(self):
        self.assertEqual(remove_duplicate([2, 2]), [2])

    def test_corner_case_all_duplicates(self):
        self.assertEqual(remove_duplicate([2, 2, 2]), [2])
