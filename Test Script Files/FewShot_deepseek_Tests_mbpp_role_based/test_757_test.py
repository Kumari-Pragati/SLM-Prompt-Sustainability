import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca']), '2')

    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_reverse_pairs(['abc']), '0')

    def test_all_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['cba', 'bca', 'abc']), '3')

    def test_no_reverse_pairs(self):
        self.assertEqual(count_reverse_pairs(['abc', 'def', 'ghi']), '0')

    def test_duplicate_elements(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'abc']), '1')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_reverse_pairs(123)
