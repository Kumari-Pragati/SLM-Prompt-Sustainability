import unittest
from mbpp_893_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Extract([['a', 'b', 'c'], ['d', 'e', 'f']]), ['c', 'f'])

    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([['hello']]), ['hello'])

    def test_list_with_single_element_sublists(self):
        self.assertEqual(Extract([['a'], ['b'], ['c']]), ['a', 'b', 'c'])

    def test_list_with_empty_sublists(self):
        self.assertEqual(Extract([['a', 'b', 'c'], [], ['d', 'e', 'f']]), ['c', 'e', 'f'])

    def test_list_with_non_list_sublists(self):
        with self.assertRaises(TypeError):
            Extract([['a', 'b', 'c'], 1, ['d', 'e', 'f']])
