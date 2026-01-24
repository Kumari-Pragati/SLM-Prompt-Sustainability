import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 0), [1, 4])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 1), [2, 5])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 2), [3, 6])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(extract_nth_element([], 0), [])
        self.assertListEqual(extract_nth_element([[1]], 0), [1])
        self.assertListEqual(extract_nth_element([[1]], 1), [])
        self.assertListEqual(extract_nth_element([[1]], 2), [])
        self.assertListEqual(extract_nth_element([[1]], -1), [])

    def test_complex_scenarios(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], -1), [])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 3), [])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], 4), [])
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6]], -2), [])
