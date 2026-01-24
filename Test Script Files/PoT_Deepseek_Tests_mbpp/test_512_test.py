import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_element_freq((1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_empty_tuple(self):
        self.assertEqual(count_element_freq(()), {})

    def test_single_element(self):
        self.assertEqual(count_element_freq((5,)), {5: 1})

    def test_nested_tuple(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 1))), {1: 2, 2: 2})

    def test_duplicate_nested_tuple(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 1), (1, 2))), {1: 2, 2: 2})

    def test_mixed_types(self):
        self.assertEqual(count_element_freq((1, 'a', 'a', 2, 2)), {1: 1, 'a': 2, 2: 2})

    def test_large_input(self):
        test_tuple = tuple(range(1, 1001)) + tuple(range(1, 1001))
        self.assertEqual(len(count_element_freq(test_tuple)), 1000)
