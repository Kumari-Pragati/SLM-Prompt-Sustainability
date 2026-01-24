import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello:World")
        self.assertEqual(replace_max_specialchar("Python, the amazing language!", 2), "Python:the:amazing:language")

    def test_edge_input(self):
        self.assertEqual(replace_max_specialchar("", 1), "")
        self.assertEqual(replace_max_specialchar("Hello, World!", 0), "Hello, World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 3), "Hello:World:!")

    def test_complex_input(self):
        self.assertEqual(replace_max_specialchar("Hello, World! It's a beautiful day.", 2), "Hello:World!: It's:a:beautiful:day.")
        self.assertEqual(replace_max_specialchar("123Hello, World!456", 2), "123Hello:World!:456")
        self.assertEqual(replace_max_specialchar("Hello, World! It's a beautiful day.", 1), "Hello:World! It's a beautiful day.")
