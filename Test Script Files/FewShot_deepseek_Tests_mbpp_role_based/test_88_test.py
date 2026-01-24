import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), collections.Counter({1: 1, 2: 2, 3: 3}))

    def test_empty_list(self):
        self.assertEqual(freq_count([]), collections.Counter())

    def test_single_element(self):
        self.assertEqual(freq_count([1]), collections.Counter({1: 1}))

    def test_duplicate_elements(self):
        self.assertEqual(freq_count([1, 1, 1, 2, 2, 3]), collections.Counter({1: 3, 2: 2, 3: 1}))

    def test_non_integer_elements(self):
        self.assertEqual(freq_count(['a', 'b', 'b', 'c']), collections.Counter({'a': 1, 'b': 2, 'c': 1}))

    def test_negative_numbers(self):
        self.assertEqual(freq_count([-1, -1, 0, 0]), collections.Counter({-1: 2, 0: 2}))
