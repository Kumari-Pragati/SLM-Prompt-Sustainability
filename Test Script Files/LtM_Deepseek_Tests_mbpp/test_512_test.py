import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_element_freq((1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_empty_input(self):
        self.assertEqual(count_element_freq(()), {})

    def test_nested_tuple(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 3), (3, 1))), {1: 2, 2: 2, 3: 1})

    def test_repeated_elements(self):
        self.assertEqual(count_element_freq((1, 1, 1, 2, 2, 3)), {1: 3, 2: 2, 3: 1})

    def test_single_element(self):
        self.assertEqual(count_element_freq((1,)), {1: 1})

    def test_mixed_types(self):
        self.assertEqual(count_element_freq((1, 'a', 'a', 2, 2, 'b')), {1: 1, 'a': 2, 2: 2, 'b': 1})
