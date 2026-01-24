import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([['a']]), ['a'])

    def test_multiple_elements_list(self):
        self.assertEqual(Extract([['a', 'b'], ['c', 'd']]), ['b', 'd'])

    def test_list_with_empty_strings(self):
        self.assertEqual(Extract([['a', ''], ['c', 'd']]), ['', 'd'])

    def test_list_with_empty_sublists(self):
        self.assertEqual(Extract([['a', []], ['c', 'd']]), ['', 'd'])

    def test_list_with_mixed_types(self):
        self.assertEqual(Extract([['a', 1, 'c'], ['d', 2, 'e']]), [1, 'e'])

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            Extract([1, 'a', 'b'])
