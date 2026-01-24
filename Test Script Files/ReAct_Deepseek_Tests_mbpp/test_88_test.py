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
        self.assertEqual(freq_count([1, 1, 1, 2, 2, 3]), collections.Counter({1: 3, 2: 2, 3: 1}))

    def test_large_list(self):
        self.assertEqual(freq_count(list(range(1, 1001))), collections.Counter({i: 1 for i in range(1, 1001)}))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            freq_count([1, 'a', 2.0])
