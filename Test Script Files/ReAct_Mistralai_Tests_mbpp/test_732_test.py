import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_replace_special_characters(self):
        self.assertEqual(replace_specialchar("Hello, World.!"), "Hello:World:!")
        self.assertEqual(replace_specialchar(""), "" )
        self.assertEqual(replace_specialchar(":"), ":")
        self.assertEqual(replace_specialchar("Hello:World:!"), "Hello:World:!")

    def test_edge_cases(self):
        self.assertEqual(replace_specialchar("Hello,World"), "Hello:World")
        self.assertEqual(replace_specialchar("Hello,World."), "Hello:World:.")
        self.assertEqual(replace_specialchar("Hello,World!!"), "Hello:World:!")
        self.assertEqual(replace_specialchar("Hello,World.."), "Hello:World:.")
        self.assertEqual(replace_specialchar("Hello,World..!"), "Hello:World:!")

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            replace_specialchar(123)
        with self.assertRaises(TypeError):
            replace_specialchar(None)
