import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(extract_elements([], 1), [])

    def test_single_element(self):
        self.assertListEqual(extract_elements([1], 1), [1])
        self.assertListEqual(extract_elements([1], 2), [])

    def test_multiple_elements(self):
        self.assertListEqual(extract_elements([1, 1, 2, 1, 3, 1, 2], 2), [(1, 1), (2, 1), (1, 2)])
        self.assertListEqual(extract_elements([1, 1, 2, 1, 3, 1, 2], 3), [(1, 1, 2), (1, 1, 1), (3, 1, 2)])
        self.assertListEqual(extract_elements([1, 1, 2, 1, 3, 1, 2], 4), [])

    def test_negative_n(self):
        self.assertListEqual(extract_elements([1, 1, 2, 1, 3, 1, 2], -1), [])

    def test_non_iterable_input(self):
        self.assertRaises(TypeError, extract_elements, "not_a_list", 1)
