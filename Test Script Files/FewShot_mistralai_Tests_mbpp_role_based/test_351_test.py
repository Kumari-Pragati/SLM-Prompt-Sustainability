import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(first_Element([], 1, 1), -1)

    def test_single_element_array(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_array_with_one_occurrence(self):
        self.assertEqual(first_Element([1, 2, 3, 1], 4, 1), 1)

    def test_array_with_multiple_occurrences(self):
        self.assertEqual(first_Element([1, 2, 1, 3, 1], 4, 1), 1)

    def test_array_with_no_matching_element(self):
        self.assertEqual(first_Element([1, 2, 3], 4, 1), -1)

    def test_array_with_k_greater_than_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 4), -1)

    def test_array_with_k_equal_to_n(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 3), 3)

    def test_array_with_negative_elements(self):
        self.assertEqual(first_Element([-1, 0, 1], 3, 1), 1)

    def test_array_with_duplicate_negative_elements(self):
        self.assertEqual(first_Element([-1, -1, -1], 3, 1), -1)
