import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_concatenate_strings_typical_case(self):
        test_tup1 = ('Hello', ' World')
        test_tup2 = ('Python', ' Test')
        expected_result = ('HelloPython', ' WorldTest')
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), expected_result)

    def test_concatenate_strings_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_result = ()
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), expected_result)

    def test_concatenate_strings_single_tuple(self):
        test_tup1 = ('Test',)
        test_tup2 = ('Case',)
        expected_result = ('TestCase',)
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), expected_result)

    def test_concatenate_strings_different_lengths(self):
        test_tup1 = ('Short', 'String')
        test_tup2 = ('Long', 'String', 'Extra')
        expected_result = ('ShortLong', 'StringStringExtra')
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), expected_result)

    def test_concatenate_strings_mixed_types(self):
        test_tup1 = ('String', 123)
        test_tup2 = ('Another', 'String')
        with self.assertRaises(TypeError):
            concatenate_strings(test_tup1, test_tup2)
