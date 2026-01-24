import unittest
from760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_unique_element_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_unique_element_multiple_elements(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'YES')

    def test_unique_element_duplicate_elements(self):
        self.assertEqual(unique_Element([1, 1, 2], 3), 'NO')

    def test_unique_element_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'NO')

    def test_unique_element_negative_list(self):
        self.assertEqual(unique_Element([-1, -2, -3], 3), 'YES')
