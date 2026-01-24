import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_concatenate_strings(self):
        test_tup1 = ('Hello', 'World')
        test_tup2 = (' ', '')
        expected_result = ('HelloWorld',)
        self.assertTupleEqual(concatenate_strings(test_tup1, test_tup2), expected_result)

    def test_concatenate_strings_with_different_lengths(self):
        test_tup1 = ('Hello', 'World', '!')
        test_tup2 = (' ', '', '!')
        expected_result = ('HelloWorld!',)
        self.assertTupleEqual(concatenate_strings(test_tup1, test_tup2), expected_result)

    def test_concatenate_strings_with_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_result = ()
        self.assertTupleEqual(concatenate_strings(test_tup1, test_tup2), expected_result)
