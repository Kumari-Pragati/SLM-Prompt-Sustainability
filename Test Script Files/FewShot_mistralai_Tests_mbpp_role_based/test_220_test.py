import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_replace_special_characters(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello:World:")
        self.assertEqual(replace_max_specialchar("This, is, a, test.", 1), "This: is: a: test.")
        self.assertEqual(replace_max_specialchar("", 1), "")
        self.assertEqual(replace_max_specialchar("Hello, World!", 3), "Hello:World::")
        self.assertEqual(replace_max_specialchar("Hello, World!", 0), "Hello, World!")
