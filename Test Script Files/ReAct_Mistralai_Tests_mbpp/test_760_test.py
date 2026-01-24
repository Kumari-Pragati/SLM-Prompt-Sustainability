import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_single_element_list(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_duplicate_elements_list(self):
        self.assertEqual(unique_Element([1, 1], 2), 'NO')

    def test_unique_elements_list(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'YES')

    def test_negative_list_length(self):
        with self.assertRaises(ValueError):
            unique_Element([1, 2, 3], -1)

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            unique_Element('abc', 3)

    def test_empty_input_element(self):
        with self.assertRaises(ValueError):
            unique_Element([], 0)
