import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((42,)), '42')

    def test_tuple_with_string_elements(self):
        self.assertEqual(concatenate_tuple(('a', 'b', 'c')), 'a-b-c')

    def test_tuple_with_mixed_types(self):
        self.assertEqual(concatenate_tuple((1, 'a', 2)), '1-a-2')

    def test_tuple_with_duplicates(self):
        self.assertEqual(concatenate_tuple((1, 2, 2, 1)), '1-2-2-1')

    def test_large_tuple(self):
        large_tuple = tuple(range(1, 1001))
        expected_result = '-'.join(map(str, large_tuple))
        self.assertEqual(concatenate_tuple(large_tuple), expected_result)
