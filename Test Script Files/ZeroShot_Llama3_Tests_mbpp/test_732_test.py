import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_replace_specialchar(self):
        self.assertEqual(replace_specialchar("Hello, World!"), "Hello: World!")
        self.assertEqual(replace_specialchar("This is a test. 123"), "This: is: a: test.: 123:")
        self.assertEqual(replace_specialchar("Special characters:!,."), "Special characters:!: :.")
        self.assertEqual(replace_specialchar("No special characters"), "No special characters")
        self.assertEqual(replace_specialchar("No special characters. 123"), "No special characters.: 123")
        self.assertEqual(replace_specialchar("No special characters, 123"), "No special characters:, 123")
