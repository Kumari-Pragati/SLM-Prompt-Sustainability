import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(concatenate_tuple((1, 2, 3)), '1-2-3')

    def test_empty_tuple(self):
        self.assertEqual(concatenate_tuple(()), '')

    def test_single_element_tuple(self):
        self.assertEqual(concatenate_tuple((42,)), '42')

    def test_string_elements(self):
        self.assertEqual(concatenate_tuple(('a', 'b', 'c')), 'a-b-c')

    def test_mixed_type_elements(self):
        self.assertEqual(concatenate_tuple((1, 'a', 3)), '1-a-3')

    def test_large_tuple(self):
        large_tuple = tuple(range(1, 1001))
        expected_result = '-'.join(map(str, large_tuple))
        self.assertEqual(concatenate_tuple(large_tuple), expected_result)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_tuple(123)

        with self.assertRaises(TypeError):
            concatenate_tuple('123')

        with self.assertRaises(TypeError):
            concatenate_tuple(None)

        with self.assertRaises(TypeError):
            concatenate_tuple([1, 2, 3])

        with self.assertRaises(TypeError):
            concatenate_tuple((1, 2, [3, 4]))
