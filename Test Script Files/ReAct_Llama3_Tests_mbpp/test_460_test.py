import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(Extract([]), [])

    def test_single_element_list(self):
        self.assertEqual(Extract([['a', 'b']]), ['a'])

    def test_multiple_elements_list(self):
        self.assertEqual(Extract([['a', 'b'], ['c', 'd']]), ['a', 'c'])

    def test_list_with_empty_sublist(self):
        self.assertEqual(Extract([['a', 'b'], ['', 'd']]), ['a'])

    def test_list_with_sublist_of_length_one(self):
        self.assertEqual(Extract([['a'], ['b']]), ['a', 'b'])

    def test_list_with_sublist_of_length_zero(self):
        self.assertEqual(Extract([['', 'b']]), [])
