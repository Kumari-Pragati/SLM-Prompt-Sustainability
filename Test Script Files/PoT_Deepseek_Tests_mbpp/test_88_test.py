import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(freq_count(['a', 'b', 'a', 'c', 'b', 'b']), {'a': 2, 'b': 3, 'c': 1})

    def test_empty_list(self):
        self.assertEqual(freq_count([]), {})

    def test_single_element(self):
        self.assertEqual(freq_count(['a']), {'a': 1})

    def test_duplicate_elements(self):
        self.assertEqual(freq_count(['a', 'a']), {'a': 2})

    def test_large_list(self):
        self.assertEqual(freq_count(list(range(1, 101))), {i: 1 for i in range(1, 101)})

    def test_mixed_case(self):
        self.assertEqual(freq_count(['a', 'A', 'a']), {'a': 2, 'A': 1})

    def test_numeric_list(self):
        self.assertEqual(freq_count([1, 2, 2, 3]), {1: 1, 2: 2, 3: 1})
