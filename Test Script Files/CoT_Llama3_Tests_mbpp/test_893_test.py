import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), ['c', 'f', 'i'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([['hello']]), ['hello'])

    def test_list_of_empty_lists(self):
        self.assertEqual(Extract([[], [], []]), [])

    def test_list_with_mixed_lengths(self):
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]), ['c', 'e', 'i'])

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            Extract([1, 2, 3])

    def test_list_with_non_string_elements(self):
        with self.assertRaises(TypeError):
            Extract([['a', 'b', 'c'], [1, 2, 3], ['d', 'e', 'f']])
