import unittest
from mbpp_22_code import find_first_duplicate

class TestFindFirstDuplicate(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 5]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(find_first_duplicate([1]), -1)

    def test_edge_case_empty_list(self):
        self.assertEqual(find_first_duplicate([]), -1)

    def test_edge_case_single_duplicate(self):
        self.assertEqual(find_first_duplicate([1, 1]), 1)

    def test_edge_case_multiple_duplicates(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 4, 4]), 2)

    def test_edge_case_duplicates_at_start(self):
        self.assertEqual(find_first_duplicate([1, 1, 2, 3, 4]), 1)

    def test_edge_case_duplicates_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 4]), 4)

    def test_edge_case_duplicates_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 4]), 2)

    def test_edge_case_duplicates_spaced(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 4, 2, 5]), 2)

    def test_edge_case_duplicates_consecutive(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3]), 2)

    def test_edge_case_duplicates_consecutive_at_start(self):
        self.assertEqual(find_first_duplicate([1, 1, 2, 3]), 1)

    def test_edge_case_duplicates_consecutive_at_end(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 3]), 3)

    def test_edge_case_duplicates_consecutive_in_middle(self):
        self.assertEqual(find_first_duplicate([1, 2, 2, 3, 3]), 2)

    def test_edge_case_duplicates_consecutive_spaced(self):
        self.assertEqual(find_first_duplicate([1, 2, 3, 2, 4]), 2)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            find_first_duplicate("abc")

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            find_first_duplicate([1, "a", 2, 3])
