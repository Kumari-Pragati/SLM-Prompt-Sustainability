import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):
    def test_concatenate_two_strings(self):
        self.assertEqual(concatenate_strings(('hello', 'world'), ('!', '?')), (('helloworld', '!?')))

    def test_concatenate_strings_of_different_lengths(self):
        self.assertEqual(concatenate_strings(('abc', 'def'), ('123', '456')), (('abc123', 'def456')))

    def test_concatenate_empty_strings(self):
        self.assertEqual(concatenate_strings(('', 'example'), ('', 'result')), (('', 'exampleresult')))

    def test_concatenate_strings_with_one_empty_string(self):
        self.assertEqual(concatenate_strings(('example', ''), ('result', '')), (('example', 'result')))

    def test_concatenate_strings_with_one_tuple_of_one_empty_string(self):
        self.assertEqual(concatenate_strings(('example',), ('', 'result')), (('example', 'result')))
