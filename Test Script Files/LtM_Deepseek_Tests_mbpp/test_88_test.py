import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(freq_count(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_empty_input(self):
        self.assertEqual(freq_count([]), {})

    def test_single_element_input(self):
        self.assertEqual(freq_count(['a']), {'a': 1})

    def test_duplicate_elements(self):
        self.assertEqual(freq_count(['a', 'a', 'b', 'b']), {'a': 2, 'b': 2})

    def test_mixed_case_elements(self):
        self.assertEqual(freq_count(['a', 'A']), {'a': 1, 'A': 1})
