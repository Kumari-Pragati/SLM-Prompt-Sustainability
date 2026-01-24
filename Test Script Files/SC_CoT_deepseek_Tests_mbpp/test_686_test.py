import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(freq_element(('a', 'b', 'c', 'a', 'b')), "{'a': 2, 'b': 2, 'c': 1}")

    def test_empty_tuple(self):
        self.assertEqual(freq_element(()), "{}")

    def test_single_element(self):
        self.assertEqual(freq_element(('a',)), "{'a': 1}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element(('a', 'a', 'a', 'b', 'b')), "{'a': 3, 'b': 2}")

    def test_large_tuple(self):
        large_tuple = ('a',) * 10000
        self.assertEqual(freq_element(large_tuple), "{'a': 10000}")

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            freq_element((1, 2, 3))

    def test_mixed_type_elements(self):
        with self.assertRaises(TypeError):
            freq_element(('a', 1, 2.0))
