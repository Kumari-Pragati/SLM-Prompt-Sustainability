import unittest
from mbpp_40_code import Counter
from itertools import chain
from 40_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(freq_element([]), {})

    def test_single_element(self):
        self.assertDictEqual(freq_element([1]), {1: 1})

    def test_multiple_elements(self):
        self.assertDictEqual(freq_element([1, 2, 1, 3, 2, 1]), {1: 3, 2: 2, 3: 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(freq_element([1, 1, 2, 2, 3, 3, 3]), {1: 2, 2: 2, 3: 3})

    def test_list_with_floats(self):
        self.assertDictEqual(freq_element([1.0, 2.0, 1.0]), {1.0: 2, 2.0: 1})

    def test_list_with_strings(self):
        self.assertDictEqual(freq_element(['a', 'b', 'a']), {'a': 2, 'b': 1})

    def test_list_with_mixed_types(self):
        self.assertDictEqual(freq_element([1, 'a', 2, 'a']), {1: 1, 'a': 2, 2: 1})

    def test_list_with_none(self):
        self.assertDictEqual(freq_element([None, None, 1]), {None: 2, 1: 1})

    def test_list_with_empty_list(self):
        self.assertDictEqual(freq_element([[], [1, 2]]), {{}: 2, 1: 1, 2: 1})
