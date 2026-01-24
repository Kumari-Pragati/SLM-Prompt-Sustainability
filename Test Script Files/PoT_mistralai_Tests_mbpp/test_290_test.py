import unittest
from mbpp_290_code import max_length

class TestMaxLength(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_length([1, 'abc', 3.14, [1, 2, 3]]), (3, 'abc'))

    def test_empty_list(self):
        self.assertEqual(max_length([]), (0, None))

    def test_single_element(self):
        self.assertEqual(max_length([1]), (1, 1))

    def test_all_same_length(self):
        self.assertEqual(max_length(['aa', 'bb', 'cc']), (2, 'bb'))

    def test_all_same_value(self):
        self.assertEqual(max_length([1, 1, 1]), (1, 1))

    def test_negative_list(self):
        self.assertEqual(max_length([-1, -2, -3]), (3, -3))

    def test_string_with_spaces(self):
        self.assertEqual(max_length(['hello', 'world', 'is', 'great']), (5, 'world'))

    def test_list_with_empty_strings(self):
        self.assertEqual(max_length(['a', '', 'b', 'c', 'd', 'e', '']), (3, 'a'))
