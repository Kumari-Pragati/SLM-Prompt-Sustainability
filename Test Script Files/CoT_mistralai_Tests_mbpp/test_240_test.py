import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_replace_list_with_same_length(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5]), [1, 2, 4, 5])
        self.assertEqual(replace_list(['a', 'b', 'c'], ['d', 'e']), ['a', 'b', 'd', 'e'])

    def test_replace_list_with_different_lengths(self):
        self.assertEqual(replace_list([1, 2, 3], [4]), [1, 2, 3, 4])
        self.assertEqual(replace_list(['a', 'b'], ['c', 'd', 'e']), ['a', 'b', 'c'])

    def test_replace_list_with_empty_list(self):
        self.assertEqual(replace_list([], [4, 5]), [4, 5])
        self.assertEqual(replace_list([1, 2], []), [1, 2])

    def test_replace_list_with_single_element(self):
        self.assertEqual(replace_list([1], [4, 5]), [4, 5])
        self.assertEqual(replace_list([4], [1, 2]), [1, 2, 4])

    def test_replace_list_with_negative_index(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5]), [1, 2, 4, 5])
        self.assertEqual(replace_list(['a', 'b', 'c'], ['d', 'e']), ['a', 'b', 'd', 'e'])

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, replace_list, [1, 2], 3)
        self.assertRaises(TypeError, replace_list, 'a', [1, 2])
