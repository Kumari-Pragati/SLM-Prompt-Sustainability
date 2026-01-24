import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_single_element_list(self):
        self.assertEqual(Extract([['a']]), ['a'])

    def test_multiple_elements_list(self):
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e', 'f']]), ['c', 'f'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            Extract([1, 2, 3])

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            Extract([['a', 2, 'c']])
