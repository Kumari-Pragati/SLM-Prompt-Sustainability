import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])

    def test_edge_boundary_conditions(self):
        self.assertEqual(extract_nth_element([], 0), [])
        self.assertEqual(extract_nth_element([[1, 2, 3]], 3), [])
        self.assertEqual(extract_nth_element([[1, 2, 3]], -1), [3])

    def test_complex_cases(self):
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), [1, 4, 7])
        self.assertEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1), [3, 6, 9])
