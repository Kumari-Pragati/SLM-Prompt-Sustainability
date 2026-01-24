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
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_duplicates(self):
        self.assertEqual(unique_Element([1, 1, 2, 2], 4), 'NO')

    def test_large_array(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 'NO')
