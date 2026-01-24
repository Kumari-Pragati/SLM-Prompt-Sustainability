import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):
    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_multiple_elements(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'NO')

    def test_empty_array(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_single_element_array(self):
        self.assertEqual(unique_Element([1, 1], 1), 'YES')

    def test_all_elements_unique(self):
        self.assertEqual(unique_Element([1, 2, 3, 4], 4), 'NO')

    def test_array_with_duplicates(self):
        self.assertEqual(unique_Element([1, 2, 2, 3], 3), 'NO')

    def test_array_with_duplicates_and_single(self):
        self.assertEqual(unique_Element([1, 2, 2, 3, 3], 4), 'NO')

    def test_array_with_duplicates_and_single_and_unique(self):
        self.assertEqual(unique_Element([1, 2, 2, 3, 3, 4], 5), 'NO')
