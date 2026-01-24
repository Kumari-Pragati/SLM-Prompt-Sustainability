import unittest
from mbpp_788_code import new_tuple

class TestNewTuple(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(new_tuple([1, 2, 3], 'a'), ([1, 2, 3, 'a']))

    def test_empty_list(self):
        self.assertEqual(new_tuple([], 'b'), ('', 'b'))

    def test_single_element_list(self):
        self.assertEqual(new_tuple([4], 'c'), ([4, 'c']))

    def test_negative_list(self):
        self.assertEqual(new_tuple([-1], 'd'), ([-1, 'd']))

    def test_string_with_spaces(self):
        self.assertEqual(new_tuple([5], ' six '), ([5, ' six ']))

    def test_empty_string(self):
        self.assertEqual(new_tuple([6], ''), ([6, '']))
