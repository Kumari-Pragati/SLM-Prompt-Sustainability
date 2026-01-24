import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2), [1, 2, 3, 4])
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5], 3), [2, 3, 4])
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5], 1), [1])
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5], 5), [5])
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5], 6), [])

    def test_edge_case(self):
        self.assertListEqual(extract_elements([], 2), [])
        self.assertListEqual(extract_elements([1], 2), [])
        self.assertListEqual(extract_elements([1, 1], 3), [])
        self.assertListEqual(extract_elements([1, 1, 1], 3), [1])
        self.assertListEqual(extract_elements([1, 1, 1, 1], 4), [1])
