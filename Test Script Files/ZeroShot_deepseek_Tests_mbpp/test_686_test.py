import unittest
from mbpp_686_code import defaultdict
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_single_element(self):
        self.assertEqual(freq_element(('a',)), "{'a': 1}")

    def test_multiple_elements(self):
        self.assertEqual(freq_element(('a', 'b', 'a', 'c', 'b', 'b')), "{'a': 2, 'b': 3, 'c': 1}")

    def test_empty_tuple(self):
        self.assertEqual(freq_element(()), "{}")

    def test_duplicate_elements(self):
        self.assertEqual(freq_element(('a', 'a', 'a', 'b', 'b', 'c')), "{'a': 3, 'b': 2, 'c': 1}")

    def test_sorted_elements(self):
        self.assertEqual(freq_element(('b', 'a', 'c', 'a', 'b', 'b')), "{'a': 2, 'b': 3, 'c': 1}")
