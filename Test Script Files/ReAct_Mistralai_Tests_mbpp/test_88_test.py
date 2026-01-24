import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(freq_count([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(freq_count([1]), {1: 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(freq_count([1, 1, 2, 2, 3]), {1: 2, 2: 2, 3: 1})

    def test_negative_numbers(self):
        self.assertDictEqual(freq_count([1, -1, 1, -1]), {1: 2, -1: 2})

    def test_large_numbers(self):
        self.assertDictEqual(freq_count([1000000, 1000000, 2000000]),
                             {1000000: 2, 2000000: 1})

    def test_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            freq_count(['a', 'b', 'c'])
