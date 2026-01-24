import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2]]), {(1, 2): 2})

    def test_edge_case_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_edge_case_single_element(self):
        self.assertEqual(unique_sublists([[1]]), {(1,): 1})

    def test_edge_case_single_element_multiple_occurrences(self):
        self.assertEqual(unique_sublists([[1], [1]]), {(1,): 2})

    def test_edge_case_duplicates(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2]]), {(1, 2): 2})

    def test_edge_case_duplicates_multiple_occurrences(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2], [2, 3]]), {(1, 2): 2, (2, 3): 1})

    def test_edge_case_duplicates_multiple_occurrences_and_empty(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2], [2, 3], []]), {(1, 2): 2, (2, 3): 1})

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            unique_sublists("Invalid input")

    def test_invalid_input_non_list_multiple_occurrences(self):
        with self.assertRaises(TypeError):
            unique_sublists([1, 2, "Invalid input"])
