import unittest
from mbpp_898_code import chain, islice
from 898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(extract_elements([], 1), [])

    def test_single_element(self):
        self.assertListEqual(extract_elements([1], 1), [1])

    def test_single_element_group(self):
        self.assertListEqual(extract_elements([1, 1], 1), [1])

    def test_multiple_elements_group(self):
        self.assertListEqual(extract_elements([1, 1, 2, 1, 2], 2), [(1, 1), (2, 2)])

    def test_mixed_group_lengths(self):
        self.assertListEqual(extract_elements([1, 1, 2, 1, 2, 3], 2), [(1, 1), (2, 2)])

    def test_single_element_in_group(self):
        self.assertListEqual(extract_elements([1, 1, 2, 1], 2), [(1, 1)])

    def test_empty_group(self):
        self.assertListEqual(extract_elements([1, 2, 3], 3), [])

    def test_negative_n(self):
        self.assertListEqual(extract_elements([1, 2, 3], -1), [])

    def test_floating_point_n(self):
        self.assertListEqual(extract_elements([1, 2, 3], 0.5), [])

    def test_non_integer_n(self):
        self.assertListEqual(extract_elements([1, 2, 3], "3"), [])
