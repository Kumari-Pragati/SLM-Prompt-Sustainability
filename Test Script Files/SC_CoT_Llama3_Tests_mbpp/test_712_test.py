import unittest
from mbpp_712_code import remove_duplicate

class TestRemoveDuplicate(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_duplicate([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(remove_duplicate([1]), [1])

    def test_edge_case_duplicates_at_start(self):
        self.assertEqual(remove_duplicate([2, 2, 3, 4, 4, 5, 6, 6]), [2, 3, 4, 5, 6])

    def test_edge_case_duplicates_at_end(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_at_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

    def test_edge_case_duplicates_at_start_and_end(self):
        self.assertEqual(remove_duplicate([2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), [2, 3, 4, 5, 6])

    def test_edge_case_duplicates_at_start_and_middle(self):
        self.assertEqual(remove_duplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_duplicates_at_end_and_middle(self):
        self.assertEqual(remove_duplicate([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            remove_duplicate("hello")

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            remove_duplicate(123)
