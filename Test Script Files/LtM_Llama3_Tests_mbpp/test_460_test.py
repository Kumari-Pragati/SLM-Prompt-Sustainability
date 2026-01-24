import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([['a']]), ['a'])

    def test_multiple_elements_list(self):
        self.assertEqual(Extract([['a', 'b', 'c']]), ['a', 'b', 'c'])

    def test_empty_string_list(self):
        self.assertEqual(Extract([['', 'b', 'c']]), ['', 'b', 'c'])

    def test_mixed_type_list(self):
        self.assertEqual(Extract([['a', 1, 'c']]), ['a', 1, 'c'])

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            Extract([1, 'b', 'c'])

    def test_list_with_non_list_elements_and_empty_string(self):
        with self.assertRaises(TypeError):
            Extract([1, '', 'c'])
