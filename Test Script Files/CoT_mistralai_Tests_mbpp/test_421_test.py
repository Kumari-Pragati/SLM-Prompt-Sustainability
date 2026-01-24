import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_multiple_elements_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_tuple_with_negative_numbers(self):
        self.assertEqual(concatenate_tuple((-1, 0, 1)), '-1-0-1')

    def test_tuple_with_floats(self):
        self.assertEqual(concatenate_tuple((1.1, 2.2, 3.3)), '1.1-2.2-3.3')

    def test_tuple_with_strings(self):
        self.assertEqual(concatenate_tuple(('a', 'b', 'c')), 'a-b-c')

    def test_tuple_with_mixed_types(self):
        self.assertEqual(concatenate_tuple((1, 'a', 2.5)), '1-a-2.5')

    def test_tuple_with_none(self):
        self.assertEqual(concatenate_tuple((1, None, 2)), '1-None-2')

    def test_tuple_with_lists(self):
        with self.assertRaises(TypeError):
            concatenate_tuple([1, 2, 3])
