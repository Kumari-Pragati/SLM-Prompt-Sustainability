import unittest
from mbpp_512_code import count_element_freq

class TestCountElementFreq(unittest.TestCase):

    def test_typical_case(self):
        test_tuple = (1, 2, 2, (3, 3, 3), 'a', 'a', (5,))
        expected_result = {1: 1, 2: 2, 3: 3, 'a': 2, 5: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_result)

    def test_empty_tuple(self):
        test_tuple = ()
        expected_result = {}
        self.assertEqual(count_element_freq(test_tuple), expected_result)

    def test_single_element(self):
        test_tuple = (1,)
        expected_result = {1: 1}
        self.assertEqual(count_element_freq(test_tuple), expected_result)

    def test_repeated_elements(self):
        test_tuple = (1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4)
        expected_result = {1: 3, 2: 2, 3: 4, 4: 4}
        self.assertEqual(count_element_freq(test_tuple), expected_result)

    def test_nested_tuple_with_repetition(self):
        test_tuple = ((1, 2), (1, 2), (3, 3), (4, 4))
        expected_result = {1: 2, 2: 2, 3: 2, 4: 2}
        self.assertEqual(count_element_freq(test_tuple), expected_result)

    def test_mixed_types(self):
        test_tuple = (1, 'a', 'a', (2, 2), 'b', 1)
        expected_result = {1: 2, 'a': 2, 2: 2, 'b': 1}
        self.assertEqual(count_element_freq(test_tuple), expected_result)
