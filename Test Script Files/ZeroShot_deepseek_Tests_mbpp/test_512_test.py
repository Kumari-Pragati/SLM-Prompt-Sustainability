import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(count_element_freq(()), {})

    def test_single_element_tuple(self):
        self.assertEqual(count_element_freq((1,)), {1: 1})

    def test_multiple_element_tuple(self):
        self.assertEqual(count_element_freq((1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_nested_tuple(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 3))), {1: 1, 2: 2, 3: 1})

    def test_mixed_types_tuple(self):
        self.assertEqual(count_element_freq((1, 'a', 'a', 2)), {1: 1, 'a': 2, 2: 1})
