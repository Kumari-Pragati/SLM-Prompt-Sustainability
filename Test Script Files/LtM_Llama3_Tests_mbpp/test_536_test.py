import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4, 5])
    def test_empty_input(self):
        self.assertEqual(nth_items([], 2), [])
    def test_single_element_input(self):
        self.assertEqual(nth_items([1], 2), [])
    def test_n_is_zero(self):
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3], 0)
    def test_n_is_negative(self):
        with self.assertRaises(TypeError):
            nth_items([1, 2, 3], -1)
    def test_n_is_greater_than_list_length(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 10), [1, 2, 3, 4, 5])
    def test_list_of_strings(self):
        self.assertEqual(nth_items(['a', 'b', 'c', 'd', 'e'], 2), ['b', 'c', 'd', 'e'])
    def test_list_of_mixed_types(self):
        self.assertEqual(nth_items([1, 'a', 3, 'b', 5], 2), ['a', 3, 'b', 5])
