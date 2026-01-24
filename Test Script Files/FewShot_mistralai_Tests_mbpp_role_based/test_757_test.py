import unittest
from mbpp_757_code import count_reverse_pairs

class TestCountReversePairs(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_reverse_pairs([]), '0')

    def test_single_element_list(self):
        self.assertEqual(count_reverse_pairs(['a']), '0')

    def test_two_elements_same(self):
        self.assertEqual(count_reverse_pairs(['a', 'a']), '1')

    def test_two_elements_different(self):
        self.assertEqual(count_reverse_pairs(['a', 'b']), '0')

    def test_three_elements_same_middle(self):
        self.assertEqual(count_reverse_pairs(['a', 'a', 'a']), '2')

    def test_three_elements_different(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c']), '0')

    def test_reverse_same(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'a']), '1')

    def test_reverse_different(self):
        self.assertEqual(count_reverse_pairs(['a', 'b', 'c', 'd']), '0')

    def test_negative_numbers(self):
        self.assertEqual(count_reverse_pairs([-1, -2, -3, -1]), '1')

    def test_mixed_numbers(self):
        self.assertEqual(count_reverse_pairs(['a', 1, 'b', 2, 'c', 3, 'd']), '0')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_reverse_pairs(123)
