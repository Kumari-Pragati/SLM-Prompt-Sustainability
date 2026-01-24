import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_concatenate_strings_typical(self):
        self.assertEqual(concatenate_strings(("hello", "world"), ("python", "unittest")), ("helloworldpythonunittest",))

    def test_concatenate_strings_empty(self):
        self.assertEqual(concatenate_strings(("", ""), ("", "")), ("",))

    def test_concatenate_strings_single(self):
        self.assertEqual(concatenate_strings(("hello",), ("world",)), ("helloworld",))

    def test_concatenate_strings_empty_tup1(self):
        self.assertEqual(concatenate_strings(("",), ("world",)), ("",))

    def test_concatenate_strings_empty_tup2(self):
        self.assertEqual(concatenate_strings(("hello",), ("",)), ("",))

    def test_concatenate_strings_empty_both(self):
        self.assertEqual(concatenate_strings(("",), ("",)), ("",))

    def test_concatenate_strings_invalid_input(self):
        with self.assertRaises(TypeError):
            concatenate_strings(None, ("world",))

    def test_concatenate_strings_invalid_input2(self):
        with self.assertRaises(TypeError):
            concatenate_strings(("hello",), None)

    def test_concatenate_strings_invalid_input3(self):
        with self.assertRaises(TypeError):
            concatenate_strings(None, None)
