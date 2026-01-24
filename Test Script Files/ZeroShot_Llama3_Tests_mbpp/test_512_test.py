import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(count_element_freq(()), {})

    def test_single_element_tuple(self):
        self.assertEqual(count_element_freq((1,)), {1: 1})

    def test_tuple_with_duplicates(self):
        self.assertEqual(count_element_freq((1, 1, 2, 2, 3)), {1: 2, 2: 2, 3: 1})

    def test_tuple_with_nested_tuples(self):
        self.assertEqual(count_element_freq(((1, 2), 3, 4, (5, 6))), {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})

    def test_tuple_with_empty_tuple(self):
        self.assertEqual(count_element_freq(((), 1, 2, (3,))), {1: 1, 2: 1, 3: 1})
