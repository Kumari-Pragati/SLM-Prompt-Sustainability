import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_specialchar("Hello, World."), "Hello:World:")
        self.assertEqual(replace_specialchar("Python"), ":Python:")
        self.assertEqual(replace_specialchar("123"), ":123:")

    def test_edge_input(self):
        self.assertEqual(replace_specialchar(""), ":")
        self.assertEqual(replace_specialchar(" ,."), "::")
        self.assertEqual(replace_specialchar("Hello, World,!"), "Hello:World:")
        self.assertEqual(replace_specialchar("Hello, World.123"), "Hello:World:123")

    def test_complex_input(self):
        self.assertEqual(replace_specialchar("Hello, World.123,!@#$%^&*()_+-="), "Hello:World:123:!@#$%^&*()_+-=")
        self.assertEqual(replace_specialchar("Hello, World.123,!@#$%^&*()_+-=,."), "Hello:World:123:!@#$%^&*()_+-=:.")
        self.assertEqual(replace_specialchar("Hello, World.123,!@#$%^&*()_+-=,.,,"), "Hello:World:123:!@#$%^&*()_+-=:.:,")
