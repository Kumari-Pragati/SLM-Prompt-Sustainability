import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element(self):
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_two_elements(self):
        self.assertEqual(count_reverse_pairs(['a', 'b']), '0')

    def test_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['a', 'ba']), '1')

    def test_multiple_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['a', 'ba', 'ca', 'ab', 'acba']), '3')

    def test_case_insensitive(self):
        self.assertEqual(count_reverse_pairs(['A', 'a', 'B', 'b']), '2')

    def test_mixed_types(self):
        self.assertEqual(count_reverse_pairs(['a', 1, 'b']), '0')
