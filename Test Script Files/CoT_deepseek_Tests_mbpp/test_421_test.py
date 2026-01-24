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
        self.assertEqual(concatenate_tuple(('abc', 'def')), 'abc-def')

    def test_mixed_types(self):
        self.assertEqual(concatenate_tuple((1, 'abc', 3.14)), '1-abc-3.14')

    def test_large_tuple(self):
        test_tup = tuple(range(1, 1001))
        expected_result = '-'.join(map(str, test_tup))
        self.assertEqual(concatenate_tuple(test_tup), expected_result)

    def test_negative_numbers(self):
        self.assertEqual(concatenate_tuple((-1, -2, -3)), '-1--2--3')

    def test_zero(self):
        self.assertEqual(concatenate_tuple((0,)), '0')
