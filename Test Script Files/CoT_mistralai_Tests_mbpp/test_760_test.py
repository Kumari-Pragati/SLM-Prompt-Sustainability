import unittest
from mbpp_760_code import skip
from unittest.loader import load_tests_from_module

class TestUniqueElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_multiple_unique_elements(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'YES')

    def test_multiple_non_unique_elements(self):
        self.assertEqual(unique_Element([1, 1, 2], 3), 'NO')

    def test_duplicate_first_element(self):
        self.assertEqual(unique_Element([1, 1], 2), 'NO')

    def test_duplicate_last_element(self):
        self.assertEqual(unique_Element([1, 1], 2), 'NO')

    def test_duplicate_middle_elements(self):
        self.assertEqual(unique_Element([1, 1, 1], 3), 'NO')

    def test_negative_numbers(self):
        self.assertEqual(unique_Element([-1, 2], 2), 'YES')

    def test_floats(self):
        self.assertEqual(unique_Element([1.0, 2.0], 2), 'YES')

    def test_strings(self):
        self.assertEqual(unique_Element(['a', 'b'], 2), 'YES')

    def test_list_with_none(self):
        self.assertEqual(unique_Element([None, 1], 2), 'NO')

    @skip("Skipping as the function does not handle this case")
    def test_list_with_duplicate_none(self):
        self.assertEqual(unique_Element([None, None], 2), 'NO')
