import unittest
from mbpp_88_code import Counter
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(freq_count([]), Counter())

    def test_single_element_list(self):
        self.assertEqual(freq_count(['a']), Counter({'a': 1}))

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count(['a', 'b', 'a']), Counter({'a': 2, 'b': 1}))

    def test_duplicate_elements_list(self):
        self.assertEqual(freq_count(['a', 'a', 'b', 'b']), Counter({'a': 2, 'b': 2}))

    def test_mixed_elements_list(self):
        self.assertEqual(freq_count(['a', 'b', 'c', 'd']), Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1}))
