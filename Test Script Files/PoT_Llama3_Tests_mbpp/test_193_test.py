import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_tuple((1, 2, 3, 2, 1)), (1, 2, 3))

    def test_edge_case_empty(self):
        self.assertEqual(remove_tuple(()), ())

    def test_edge_case_single_element(self):
        self.assertEqual(remove_tuple((1,)), (1,))

    def test_edge_case_duplicates(self):
        self.assertEqual(remove_tuple((1, 1, 2, 2, 3, 3)), (1, 2, 3))

    def test_edge_case_duplicates_and_empty(self):
        self.assertEqual(remove_tuple(()), ())

    def test_edge_case_duplicates_and_single_element(self):
        self.assertEqual(remove_tuple((1, 1, 2)), (1, 2))

    def test_edge_case_duplicates_and_duplicates(self):
        self.assertEqual(remove_tuple((1, 1, 1, 2, 2, 3)), (1, 2, 3))

    def test_edge_case_duplicates_and_duplicates_and_empty(self):
        self.assertEqual(remove_tuple((1, 1, 1, 2, 2, 3,)), (1, 2, 3))
