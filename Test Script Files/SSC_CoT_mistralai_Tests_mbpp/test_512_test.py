import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_typical_input(self):
        self.assertDictEqual(count_element_freq((1, 2, (3, 3, 4), 2, 3)), {'1': 1, '2': 1, '3': 2, '4': 1})
        self.assertDictEqual(count_element_freq([1, 2, (3, 3, 4), 2, 3]), {'1': 1, '2': 2, '3': 3, '4': 1})

    def test_edge_and_boundary_conditions(self):
        self.assertDictEqual(count_element_freq((1, )), {'1': 1})
        self.assertDictEqual(count_element_freq((1, 2, )), {'1': 1, '2': 1})
        self.assertDictEqual(count_element_freq((1, 2, 1)), {'1': 2, '2': 1})
        self.assertDictEqual(count_element_freq((1, 2, 1, 1)), {'1': 3, '2': 1})
        self.assertDictEqual(count_element_freq((1, 2, 1, 1, 1)), {'1': 4, '2': 1})
        self.assertDictEqual(count_element_freq((1, 2, 1, 1, 1, 1)), {'1': 5, '2': 1})
        self.assertDictEqual(count_element_freq((1, 2, 1, 1, 1, 1, 1)), {'1': 6, '2': 1})

        self.assertDictEqual(count_element_freq((1, 2, 1, 1, 1, 1, 1, 1)), {'1': 7, '2': 1})  # Check if it can handle large inputs

    def test_special_cases(self):
        self.assertDictEqual(count_element_freq((1, 1, 2, 2, 3, 3, 4, 4)), {'1': 2, '2': 2, '3': 2, '4': 2})
        self.assertDictEqual(count_element_freq((1, 1, 2, 2, 3, 3, 4, 4, 4)), {'1': 2, '2': 2, '3': 2, '4': 3})

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_element_freq, 123)  # Non-iterable input
        self.assertRaises(TypeError, count_element_freq, (1, 2, 3, 'a'))  # Mixed types
