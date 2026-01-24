import unittest
from mbpp_484_code import remove_matching_tuple

class TestRemoveMatchingTuple(unittest.TestCase):
    def test_simple_valid_input(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3], [2, 4]), [1, 3])

    def test_empty_input(self):
        self.assertEqual(remove_matching_tuple([], [1, 2]), [])
        self.assertEqual(remove_matching_tuple([1, 2], []), [1, 2])

    def test_single_element_input(self):
        self.assertEqual(remove_matching_tuple([1], [2]), [1])
        self.assertEqual(remove_matching_tuple([1], []), [1])
        self.assertEqual(remove_matching_tuple([], [1]), [])

    def test_duplicates_in_input(self):
        self.assertEqual(remove_matching_tuple([1, 2, 2], [2]), [1])
        self.assertEqual(remove_matching_tuple([1, 2, 2], []), [1, 2, 2])

    def test_empty_output(self):
        self.assertEqual(remove_matching_tuple([1, 2, 3], [1, 2, 3]), [])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            remove_matching_tuple('test', [1, 2])

    def test_invalid_input_value_type(self):
        with self.assertRaises(TypeError):
            remove_matching_tuple([1, 'test'], [1, 2])
