import unittest
from mbpp_413_code import extract_nth_element

class TestExtractNthElement(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), [2, 5, 8])
        self.assertListEqual(extract_nth_element([[0, 1, 2], [3, 4, 5], [6, 7, 8]], 2), [4, 5, 7])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(extract_nth_element([[1, 2, 3]], 0), [1])
        self.assertListEqual(extract_nth_element([[1, 2, 3]], 2), [3])
        self.assertListEqual(extract_nth_element([[1, 2, 3]], 3), [])
        self.assertListEqual(extract_nth_element([], 0), [])
        self.assertListEqual(extract_nth_element([[1, 2, 3]], -1), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_nth_element(1, 0)
        with self.assertRaises(TypeError):
            extract_nth_element('str', 0)
        with self.assertRaises(ValueError):
            extract_nth_element([[1, 2, 3]], 4)
