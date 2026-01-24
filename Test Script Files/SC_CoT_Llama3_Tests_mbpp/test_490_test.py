import unittest
from mbpp_490_code import extract_symmetric

class TestExtractSymmetric(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 3), (3, 4)]), {(1, 2), (2, 3), (3, 4)})

    def test_edge_case_empty_list(self):
        self.assertEqual(extract_symmetric([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(extract_symmetric([(1, 1)]), [])

    def test_edge_case_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1)]), [])

    def test_edge_case_duplicates_with_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2)]), [])

    def test_edge_case_duplicates_with_duplicates_and_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2), (2, 1)]), [])

    def test_edge_case_duplicates_with_duplicates_and_duplicates_and_duplicates(self):
        self.assertEqual(extract_symmetric([(1, 2), (2, 1), (1, 2), (2, 1), (1, 2)]), [])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            extract_symmetric("Invalid Input")

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            extract_symmetric([1, 2, 3])

    def test_invalid_input_non_tuple_element(self):
        with self.assertRaises(TypeError):
            extract_symmetric([("a", "b"), "c"])

    def test_invalid_input_non_tuple_element_type(self):
        with self.assertRaises(TypeError):
            extract_symmetric([("a", "b"), (1, 2, 3)])
