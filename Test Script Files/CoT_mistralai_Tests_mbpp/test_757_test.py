import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_simple_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c']), '2')

    def test_duplicate_elements_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'a', 'b', 'c']), '1')

    def test_reverse_pairs_list(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'ba']), '1')

    def test_list_with_numbers(self):
        self.assertEqual(count_reverse_pairs([1, 2, 3]), '0')

    def test_list_with_mixed_types(self):
        self.assertEqual(count_reverse_pairs(['a', 1, 'b']), '0')

    def test_list_with_non_string_elements(self):
        self.assertRaises(TypeError, count_reverse_pairs, [1, 2, 3.14])
