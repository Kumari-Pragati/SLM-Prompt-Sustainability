import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_freq((1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_empty_tuple(self):
        self.assertEqual(count_element_freq(()), {})

    def test_single_element(self):
        self.assertEqual(count_element_freq((1,)), {1: 1})

    def test_nested_tuple(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 3))), {1: 1, 2: 2, 3: 1})

    def test_duplicate_elements(self):
        self.assertEqual(count_element_freq((1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_mixed_types(self):
        self.assertEqual(count_element_freq((1, 'a', 'a', 2)), {1: 1, 'a': 2, 2: 1})

    def test_large_tuple(self):
        large_tuple = (i for i in range(1, 10001))
        self.assertEqual(len(count_element_freq(large_tuple)), 10000)
