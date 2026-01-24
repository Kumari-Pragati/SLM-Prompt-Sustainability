import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(count_element_freq(()), {})

    def test_single_element(self):
        self.assertEqual(count_element_freq((1,)), {1: 1})

    def test_multiple_elements(self):
        self.assertEqual(count_element_freq((1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_nested_tuples(self):
        self.assertEqual(count_element_freq(((1, 2), (2, 3), (3, 1))), {1: 1, 2: 2, 3: 2})

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            count_element_freq("hello")

    def test_mixed_input(self):
        self.assertEqual(count_element_freq((1, 2, "hello", 2, 3, 3)), {1: 1, 2: 2, 3: 2, "hello": 1})
