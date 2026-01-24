import unittest
from mbpp_88_code import freq_count

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(freq_count([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(freq_count(['a']), {'a': 1})

    def test_multiple_elements_list(self):
        self.assertDictEqual(freq_count(['a', 'b', 'a', 'c', 'a']), {'a': 3, 'b': 1, 'c': 1})

    def test_duplicate_elements_list(self):
        self.assertDictEqual(freq_count([1, 2, 1, 2, 1, 3, 1]), {1: 4, 2: 2, 3: 1})

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            freq_count(123)
