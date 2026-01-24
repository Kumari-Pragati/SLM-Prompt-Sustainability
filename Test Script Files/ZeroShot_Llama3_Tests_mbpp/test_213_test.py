import unittest
from mbpp_213_code import concatenate_strings

class TestConcatenateStrings(unittest.TestCase):

    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings(("Hello", "World"), ("Python", "Unittest")), ("HelloPython", "WorldUnittest"))
        self.assertEqual(concatenate_strings(("Test", "Function"), ("Pass", "Fail")), ("TestPass", "FunctionFail"))
        self.assertEqual(concatenate_strings(("", ""), ("", "")), ("", ""))
        self.assertEqual(concatenate_strings(("", "Test"), ("", "Function")), ("", "TestFunction"))
        self.assertEqual(concatenate_strings(("Test", ""), ("Function", "")), ("Test", "Function"))

    def test_concatenate_strings_empty(self):
        self.assertEqual(concatenate_strings(("",), ("",)), ("",))
        self.assertEqual(concatenate_strings(("",), ("",)), ("",))
