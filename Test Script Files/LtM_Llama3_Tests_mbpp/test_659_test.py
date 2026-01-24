import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(Repeat([]), [])

    def test_single_element_input(self):
        self.assertEqual(Repeat([1]), [])

    def test_repeated_elements(self):
        self.assertEqual(Repeat([1, 1, 2, 2, 3]), [1, 2])

    def test_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4, 5]), [])

    def test_repeated_elements_with_duplicates(self):
        self.assertEqual(Repeat([1, 1, 1, 2, 2, 3, 3, 3]), [1, 2, 3])

    def test_edge_case_empty_input(self):
        self.assertEqual(Repeat([]), [])

    def test_edge_case_single_element_input(self):
        self.assertEqual(Repeat([1]), [])

    def test_edge_case_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4, 5]), [])

    def test_edge_case_repeated_elements(self):
        self.assertEqual(Repeat([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]), [1, 2, 3])
