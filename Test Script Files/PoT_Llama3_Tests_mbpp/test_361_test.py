import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(remove_empty([1]), [1])

    def test_edge_case_multiple_empty_elements(self):
        self.assertEqual(remove_empty([0, 0, 0, 0]), [0, 0, 0, 0])

    def test_edge_case_single_empty_element(self):
        self.assertEqual(remove_empty([0]), [])

    def test_edge_case_multiple_non_empty_elements(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_mixed_elements(self):
        self.assertEqual(remove_empty([1, 0, 2, 3, 0, 4, 5]), [1, 2, 3, 4, 5])

    def test_edge_case_non_empty_and_empty_elements(self):
        self.assertEqual(remove_empty([1, 0, 2, 3, 0, 4, 5]), [1, 2, 3, 4, 5])
