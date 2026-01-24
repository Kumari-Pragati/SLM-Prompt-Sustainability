import unittest
from mbpp_686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(freq_element(('a', 'b', 'c', 'a', 'b')), "{'a': 2, 'b': 2, 'c': 1}")

    def test_empty_input(self):
        self.assertEqual(freq_element(()), "{}")

    def test_single_element_input(self):
        self.assertEqual(freq_element(('a',)), "{'a': 1}")

    def test_repeated_elements(self):
        self.assertEqual(freq_element(('a', 'a', 'b', 'b', 'c')), "{'a': 2, 'b': 2, 'c': 1}")

    def test_large_input(self):
        test_tup = ('a',) * 100000 + ('b',) * 50000 + ('c',) * 20000
        self.assertEqual(freq_element(test_tup), "{'a': 100000, 'b': 50000, 'c': 20000}")
