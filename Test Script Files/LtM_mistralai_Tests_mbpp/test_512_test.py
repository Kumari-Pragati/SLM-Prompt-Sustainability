import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_simple(self):
        self.assertDictEqual(count_element_freq((1, 2, 1, 3, 2, 2)), {'1': 2, '2': 3, '3': 1})
        self.assertDictEqual(count_element_freq(('a', 'b', 'a', 'c', 'b', 'b')), {'a': 2, 'b': 3, 'c': 1})

    def test_edge_cases(self):
        self.assertDictEqual(count_element_freq((1,)), {'1': 1})
        self.assertDictEqual(count_element_freq(()), {})
        self.assertDictEqual(count_element_freq((1, 1, 1)), {'1': 3})
        self.assertDictEqual(count_element_freq((1, 'a', 1)), {'1': 2, 'a': 1})

    def test_complex(self):
        self.assertDictEqual(count_element_freq(((1, 2), (1, 3), (1, 2))), {'1': 3, '2': 3, '3': 1})
        self.assertDictEqual(count_element_freq((1, (2, 3), 1)), {'1': 2, (2, 3): 1})
        self.assertDictEqual(count_element_freq((1, 2, (3, 4))), {'1': 1, '2': 1, (3, 4): 1})
