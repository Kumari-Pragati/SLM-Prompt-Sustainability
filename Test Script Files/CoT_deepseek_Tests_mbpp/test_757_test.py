import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca']), '3')

    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element(self):
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_same_elements(self):
        self.assertEqual(count_reverse_pairs(['abc', 'abc', 'abc']), '0')

    def test_reverse_elements(self):
        self.assertEqual(count_reverse_pairs(['abc', 'cba', 'bca']), '3')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_reverse_pairs(123)

        with self.assertRaises(TypeError):
            count_reverse_pairs(['abc', 123])

        with self.assertRaises(TypeError):
            count_reverse_pairs(['abc', 'cba', ['bca']])
