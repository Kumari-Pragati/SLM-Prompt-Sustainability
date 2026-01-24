import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_empty_list_zero_length(self):
        self.assertEqual(empty_list(0), [])

    def test_empty_list_positive_length(self):
        self.assertEqual(empty_list(5), [{}, {}, {}, {}, {}])

    def test_empty_list_negative_length(self):
        with self.assertRaises(ValueError):
            empty_list(-1)

    def test_empty_list_non_integer_input(self):
        with self.assertRaises(TypeError):
            empty_list('abc')

    def test_empty_list_zero_length_with_dict(self):
        self.assertEqual(empty_list(0, dict), [])

    def test_empty_list_positive_length_with_dict(self):
        self.assertEqual(empty_list(5, dict), [{}, {}, {}, {}, {}])

    def test_empty_list_negative_length_with_dict(self):
        with self.assertRaises(ValueError):
            empty_list(-1, dict)

    def test_empty_list_non_integer_input_with_dict(self):
        with self.assertRaises(TypeError):
            empty_list('abc', dict)
