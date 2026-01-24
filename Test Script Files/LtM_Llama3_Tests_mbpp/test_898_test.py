import unittest
from mbpp_898_code import extract_elements

class TestExtractElements(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(extract_elements([], 1), [])

    def test_single_element(self):
        self.assertEqual(extract_elements([1], 1), [1])

    def test_single_group(self):
        self.assertEqual(extract_elements([1, 1, 1], 1), [1])

    def test_multiple_groups(self):
        self.assertEqual(extract_elements([1, 2, 2, 3, 3, 3], 2), [2, 3])

    def test_group_size_1(self):
        self.assertEqual(extract_elements([1, 2, 3], 1), [1, 2, 3])

    def test_group_size_greater_than_input(self):
        self.assertEqual(extract_elements([1, 2, 3], 4), [])

    def test_group_size_equal_to_input(self):
        self.assertEqual(extract_elements([1, 1, 1, 2, 2, 2], 2), [1, 2])

    def test_group_size_greater_than_input_and_empty_input(self):
        self.assertEqual(extract_elements([], 4), [])

    def test_group_size_greater_than_input_and_single_element(self):
        self.assertEqual(extract_elements([1], 4), [])
