import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_multiple_elements(self):
        self.assertEqual(unique_Element([1, 2, 3], 3), 'NO')

    def test_single_element_array(self):
        self.assertEqual(unique_Element([1, 1, 1], 3), 'YES')

    def test_empty_array(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_array_with_duplicates(self):
        self.assertEqual(unique_Element([1, 2, 2, 3], 4), 'NO')

    def test_array_with_duplicates_and_single_element(self):
        self.assertEqual(unique_Element([1, 1, 2, 3], 4), 'NO')

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            unique_Element('hello', 1)

    def test_invalid_input_type2(self):
        with self.assertRaises(TypeError):
            unique_Element([1, 2, 3], 'hello')
