import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(freq_count([]), collections.Counter())

    def test_single_element_list(self):
        self.assertEqual(freq_count([1]), collections.Counter({1: 1}))

    def test_multiple_elements_list(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), collections.Counter({1: 1, 2: 2, 3: 3}))

    def test_list_with_duplicates(self):
        self.assertEqual(freq_count([1, 1, 2, 2, 2, 3, 3, 3, 3]), collections.Counter({1: 2, 2: 3, 3: 4}))

    def test_list_with_non_integer_elements(self):
        self.assertEqual(freq_count(['a', 'b', 'b', 'c', 'c', 'c']), collections.Counter({'a': 1, 'b': 2, 'c': 3}))

    def test_list_with_mixed_types(self):
        self.assertEqual(freq_count([1, 'a', 'b', 'b', 2, 2, 3, 3, 3]), collections.Counter({1: 1, 'a': 1, 'b': 2, 2: 2, 3: 3}))
