import unittest
from mbpp_88_code import Counter
from 88_code import freq_count

class TestFreqCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(freq_count([1, 2, 2, 3, 3, 3]), {1: 1, 2: 2, 3: 3})

    def test_empty_list(self):
        self.assertDictEqual(freq_count([]), {})

    def test_single_element(self):
        self.assertDictEqual(freq_count([4]), {4: 1})

    def test_negative_numbers(self):
        self.assertDictEqual(freq_count([-1, -2, -2]), {-1: 1, -2: 2})

    def test_floats(self):
        self.assertDictEqual(freq_count([1.1, 1.1, 2.2]), {1.1: 2, 2.2: 1})

    def test_duplicate_floats(self):
        self.assertDictEqual(freq_count([1.1, 1.1, 2.2, 2.2]), {1.1: 2, 2.2: 2})
