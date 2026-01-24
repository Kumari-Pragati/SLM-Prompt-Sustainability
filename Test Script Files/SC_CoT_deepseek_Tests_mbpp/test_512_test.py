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

    def test_duplicate_elements(self):
        self.assertEqual(count_element_freq((1, 1, 2, 2, 3, 3, 3)), {1: 2, 2: 2, 3: 3})

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            count_element_freq((1, "a", 2.0))
