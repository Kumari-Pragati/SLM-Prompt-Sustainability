import unittest
from mbpp_351_code import first_Element

class TestFirstElement(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(first_Element([], 0, 1), -1)

    def test_single_element(self):
        self.assertEqual(first_Element([1], 1, 1), 1)

    def test_multiple_elements_single_occurrence(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 1), 1)

    def test_multiple_elements_multiple_occurrences(self):
        self.assertEqual(first_Element([1, 1, 2, 3], 4, 2), 1)

    def test_array_with_no_matching_element(self):
        self.assertEqual(first_Element([1, 2, 3], 3, 4), -1)

    def test_array_with_k_greater_than_n(self):
        with self.assertRaises(ValueError):
            first_Element([1, 2, 3], 3, 4)

    def test_array_with_negative_elements(self):
        self.assertEqual(first_Element([-1, 2, 3], 3, 1), -1)

    def test_array_with_zero(self):
        self.assertEqual(first_Element([0, 1, 2], 3, 1), 1)

    def test_array_with_duplicate_zero(self):
        self.assertEqual(first_Element([0, 0, 1, 2], 4, 2), 0)
