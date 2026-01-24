import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_replace_specialchar(self):
        self.assertEqual(replace_specialchar("Hello, World!"), "Hello:World:")
        self.assertEqual(replace_specialchar("Python.Programming"), "Python:Programming")
        self.assertEqual(replace_specialchar("No, spaces, here."), "No:spaces,here:")
        self.assertEqual(replace_specialchar("Just a normal sentence."), "Just:a:normal:sentence:")
