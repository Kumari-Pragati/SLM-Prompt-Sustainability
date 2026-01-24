import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialChar(unittest.TestCase):

    def test_replace_max_specialchar(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello:World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello:,World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 3), "Hello::World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 4), "Hello:::World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 5), "Hello:::World!")
        self.assertEqual(replace_max_specialchar("Hello, World!.", 6), "Hello:::World!:.")
        self.assertEqual(replace_max_specialchar("Hello, World!..", 7), "Hello:::World!::")
