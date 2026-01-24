import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):

    def test_extract_list(self):
        self.assertEqual(Extract([['a', 'b'], ['c', 'd']]), ['a', 'c'])

    def test_extract_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_extract_single_element_list(self):
        self.assertEqual(Extract([['a']]), ['a'])

    def test_extract_list_with_multiple_elements(self):
        self.assertEqual(Extract([['a', 'b'], ['c', 'd'], ['e', 'f']]), ['a', 'c', 'e'])

    def test_extract_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            Extract([1, 2, 3])
