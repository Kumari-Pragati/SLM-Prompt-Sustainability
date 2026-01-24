import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((1,)), '1')

    def test_multiple_elements_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_negative_numbers_in_tuple(self):
        self.assertEqual(concatenate_tuple((-1, 2, -3)), '-1-2--3')

    def test_mixed_types_in_tuple(self):
        self.assertEqual(concatenate_tuple(('a', 1, 2.5)), 'a-1-2.5')

    def test_tuple_with_only_strings(self):
        self.assertEqual(concatenate_tuple(('hello', 'world', '!'))) , 'hello-world-!'
