import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_unique_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_unique_multiple_elements(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'YES')

    def test_unique_empty_list(self):
        self.assertEqual(unique_Element([], 0), 'NO')

    def test_unique_duplicates(self):
        self.assertEqual(unique_Element([1, 1, 2], 3), 'NO')

    def test_unique_large_list(self):
        self.assertEqual(unique_Element([1000000001, 1000000002, 1000000003], 3), 'YES')

    def test_unique_negative_numbers(self):
        self.assertEqual(unique_Element([-1, -2, -3], 3), 'YES')

    def test_unique_floats(self):
        self.assertEqual(unique_Element([1.1, 2.2, 3.3], 3), 'YES')

    def test_unique_strings(self):
        self.assertEqual(unique_Element(['a', 'b', 'c'], 3), 'YES')

    def test_unique_mixed_data_types(self):
        self.assertEqual(unique_Element([1, 'a', 2.0], 3), 'NO')

    def test_unique_invalid_input_list(self):
        with self.assertRaises(TypeError):
            unique_Element('abc', 3)

    def test_unique_invalid_input_length(self):
        with self.assertRaises(ValueError):
            unique_Element([1, 2, 3], 0)
