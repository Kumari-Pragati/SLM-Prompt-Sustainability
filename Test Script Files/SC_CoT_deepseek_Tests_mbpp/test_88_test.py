import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(freq_count([1, 2, 2, 3, 3, 3]), collections.Counter({1: 1, 2: 2, 3: 3}))

    def test_empty_list(self):
        self.assertEqual(freq_count([]), collections.Counter())

    def test_single_element(self):
        self.assertEqual(freq_count([1]), collections.Counter({1: 1}))

    def test_duplicate_elements(self):
        self.assertEqual(freq_count(['a', 'a', 'b', 'b']), collections.Counter({'a': 2, 'b': 2}))

    def test_mixed_types(self):
        self.assertEqual(freq_count(['a', 1, 1, 'a']), collections.Counter({'a': 2, 1: 2}))

    def test_negative_numbers(self):
        self.assertEqual(freq_count([-1, -1, 1, 1]), collections.Counter({-1: 2, 1: 2}))

    def test_zero(self):
        self.assertEqual(freq_count([0, 0, 1, 1]), collections.Counter({0: 2, 1: 2}))

    def test_large_numbers(self):
        self.assertEqual(freq_count([1000, 1000, 2000, 2000]), collections.Counter({1000: 2, 2000: 2}))

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            freq_count(123)

    def test_none_input(self):
        with self.assertRaises(TypeError):
            freq_count(None)
