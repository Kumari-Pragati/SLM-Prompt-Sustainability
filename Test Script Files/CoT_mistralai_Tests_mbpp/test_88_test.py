import unittest
from mbpp_88_code import Counter
from 88_code import freq_count

class TestFreqCount(unittest.TestCase):
    def test_empty_list(self):
        self.assertDictEqual(freq_count([]), {})

    def test_single_element(self):
        self.assertDictEqual(freq_count([1]), {1: 1})

    def test_multiple_elements(self):
        self.assertDictEqual(freq_count([1, 2, 1, 3, 2, 2]), {1: 2, 2: 3, 3: 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(freq_count([1, 1, 2, 2, 3, 3, 3]), {1: 2, 2: 2, 3: 3})

    def test_negative_numbers(self):
        self.assertDictEqual(freq_count([-1, -2, -1, 0, 1]), {-1: 2, -2: 1, 0: 1, 1: 1})

    def test_floats(self):
        self.assertAlmostEqual(freq_count([1.1, 2.2, 1.1, 3.3, 2.2, 2.2]), {1.1: 2, 2.2: 3, 3.3: 1})

    def test_strings(self):
        self.assertDictEqual(freq_count(['a', 'b', 'a', 'c', 'b', 'b']), {'a': 2, 'b': 3, 'c': 1})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            freq_count(123)
