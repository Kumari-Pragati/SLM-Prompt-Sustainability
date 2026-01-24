import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = ('Hello', 'World')
        test_tup2 = ('Python', 'Programming')
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), ('HelloPython', 'WorldProgramming'))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), ())

    def test_tuples_of_different_lengths(self):
        test_tup1 = ('Hello', 'World')
        test_tup2 = ('Python', 'Programming', 'Language')
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), ('HelloPython', 'WorldProgramming', 'Language'))

    def test_tuples_with_single_elements(self):
        test_tup1 = ('Hello')
        test_tup2 = ('World')
        self.assertEqual(concatenate_strings(test_tup1, test_tup2), ('HelloWorld',))
