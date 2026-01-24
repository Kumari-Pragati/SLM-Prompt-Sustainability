import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_typical_case(self):
        self.assertDictEqual(count_element_freq((1, 2, 3, 1, 2, 3)), {'1': 2, '2': 2, '3': 2})
        self.assertDictEqual(count_element_freq([1, 2, 3, 1, 2, 3]), {'1': 2, '2': 2, '3': 2})
        self.assertDictEqual(count_element_freq({'a': 1, 'b': 2, 'c': 3, 'a': 1, 'b': 2, 'c': 3}), {'a': 2, 'b': 2, 'c': 3})

    def test_edge_case_empty(self):
        self.assertDictEqual(count_element_freq([]), {})
        self.assertDictEqual(count_element_freq(()), {})
        self.assertDictEqual(count_element_freq({}), {})

    def test_edge_case_single_element(self):
        self.assertDictEqual(count_element_freq((1,)), {'1': 1})
        self.assertDictEqual(count_element_freq([1]), {'1': 1})
        self.assertDictEqual(count_element_freq({'a': 1}), {'a': 1})

    def test_edge_case_duplicate_elements(self):
        self.assertDictEqual(count_element_freq((1, 1, 2, 2, 3, 3)), {'1': 2, '2': 2, '3': 2})
        self.assertDictEqual(count_element_freq([1, 1, 2, 2, 3, 3]), {'1': 2, '2': 2, '3': 2})
        self.assertDictEqual(count_element_freq({'a': 1, 'a': 1, 'b': 2, 'b': 2, 'c': 3, 'c': 3}), {'a': 2, 'b': 2, 'c': 3})

    def test_corner_case_nested_tuples(self):
        self.assertDictEqual(count_element_freq(((1,), (2, 2), (3, 3, 3))), {'(1,)': 1, '(2,)': 1, '(3,)': 3, '3': 3})
        self.assertDictEqual(count_element_freq([[1], [2, 2], [3, 3, 3]]) , {'[1]': 1, '[2, 2]': 1, '[3, 3, 3]': 1, '3': 3})
        self.assertDictEqual(count_element_freq({('a',): 1, (('b',),): 2, (('c', 'c', 'c')): 3}), {('a',): 1, (('b',),): 2, (('c', 'c', 'c')): 3})
