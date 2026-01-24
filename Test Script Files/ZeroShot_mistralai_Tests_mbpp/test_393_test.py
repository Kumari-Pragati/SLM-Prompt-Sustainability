import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_single_element_list(self):
        self.assertEqual(max_length_list(['a']), (1, ['a']))

    def test_multiple_elements_same_length(self):
        self.assertEqual(max_length_list(['aa', 'bb', 'cc']), (2, ['aa', 'bb', 'cc']))

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(max_length_list(['aa', 'ab', 'abc']), (3, ['aa', 'ab', 'abc']))

    def test_negative_strings(self):
        self.assertEqual(max_length_list(['aa', '-ab', 'abc']), (3, ['aa', '-ab', 'abc']))

    def test_empty_strings(self):
        self.assertEqual(max_length_list(['', 'aa', 'abc']), (2, ['aa', 'abc']))

    def test_list_with_numbers(self):
        self.assertEqual(max_length_list(['aa', 1, 'abc']), (3, ['aa', 'abc']))
