import unittest
from mbpp_758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2]]), {(1, 2): 2, (2, 3): 1})

    def test_edge_case_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_edge_case_single_list(self):
        self.assertEqual(unique_sublists([[1, 2, 3]]), {(1, 2, 3): 1})

    def test_edge_case_single_element(self):
        self.assertEqual(unique_sublists([[1]]), {(1,): 1})

    def test_edge_case_duplicates(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1], [1, 2]]), {(1, 2): 2})

    def test_edge_case_empty_sublist(self):
        self.assertEqual(unique_sublists([[1, 2], [], [1, 2]]), {(1, 2): 2})

    def test_edge_case_sublist_duplicates(self):
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 3})
