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

    def test_mixed_case(self):
        self.assertEqual(freq_element(('a', 'A', 'a', 'B', 'b')), "{'a': 2, 'A': 1, 'b': 1, 'B': 1}")

    def test_large_tuple(self):
        test_tup = tuple('a'*10000 + 'b'*10000)
        self.assertEqual(freq_element(test_tup)[:-1], "{'a': 10000, 'b': 10000}")
