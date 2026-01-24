import unittest
from mbpp_898_code import chain, islice, repeat
from 898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2), [1, 2, 3, 4])
        self.assertListEqual(extract_elements([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6], 3), [2, 3, 4])

    def test_edge_and_boundary_conditions(self):
        self.assertListEqual(extract_elements([], 1), [])
        self.assertListEqual(extract_elements([1], 1), [1])
        self.assertListEqual(extract_elements([1, 1], 1), [1])
        self.assertListEqual(extract_elements([1, 1, 1], 1), [1])
        self.assertListEqual(extract_elements([1, 1, 1, 1], 1), [1])
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1], 1), [1])
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1, 1], 2), [1, 1])
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1, 1, 1], 3), [])
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1, 1, 1, 1], 4), [])
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1, 1, 1, 1, 1], 5), [])
        self.assertListEqual(extract_elements([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 6), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, extract_elements, (1, 2), 3)
        self.assertRaises(TypeError, extract_elements, [1, 2], 'n')
