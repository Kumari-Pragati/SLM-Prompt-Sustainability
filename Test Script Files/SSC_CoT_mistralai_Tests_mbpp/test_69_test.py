import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))
        self.assertTrue(is_sublist([], [1, 2, 3]))
        self.assertFalse(is_sublist([], [4, 5, 6]))

    def test_equal_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))
        self.assertTrue(is_sublist([3, 2, 1], [1, 2, 3]))

    def test_longer_sublist(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 3, 4]))
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 3, 4, 5]))

    def test_shorter_sublist(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2]))
        self.assertTrue(is_sublist([1, 2, 3], [2, 3]))
        self.assertFalse(is_sublist([1, 2, 3], [4, 5]))

    def test_mixed_types(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 'a', 3]))
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 'a']))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, is_sublist, 'list1', [1, 2, 3])
        self.assertRaises(TypeError, is_sublist, [1, 2, 3], 'list2')
