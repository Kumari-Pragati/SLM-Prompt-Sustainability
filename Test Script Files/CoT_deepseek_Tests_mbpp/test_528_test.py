import unittest
from mbpp_528_code import min_length

class TestMinLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_length(['abc', 'defgh', 'ijklm']), (3, 'abc'))

    def test_single_element(self):
        self.assertEqual(min_length(['abc']), (3, 'abc'))

    def test_empty_list(self):
        self.assertEqual(min_length([]), (0, ''))

    def test_all_empty_strings(self):
        self.assertEqual(min_length(['', '']), (0, ''))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            min_length(['abc', 123, 'def'])

    def test_none_in_list(self):
        with self.assertRaises(TypeError):
            min_length(['abc', None, 'def'])
