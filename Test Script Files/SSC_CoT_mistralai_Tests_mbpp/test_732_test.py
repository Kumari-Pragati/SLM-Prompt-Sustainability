import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialChar(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(replace_specialchar("Hello, World."), "Hello:World:")
        self.assertEqual(replace_specialchar("1,2,3."), "1:2:3:")
        self.assertEqual(replace_specialchar("A, B, C."), "A: B: C:")

    def test_edge_cases(self):
        self.assertEqual(replace_specialchar(""), "")
        self.assertEqual(replace_specialchar("Hello"), "Hello:")
        self.assertEqual(replace_specialchar("Hello,"), "Hello:")
        self.assertEqual(replace_specialchar("Hello."), "Hello:")
        self.assertEqual(replace_specialchar("Hello, World"), "Hello:World:")
        self.assertEqual(replace_specialchar("Hello, World."), "Hello:World:")

    def test_boundary_cases(self):
        self.assertEqual(replace_specialchar("Hello, World!"), "Hello:World:!")
        self.assertEqual(replace_specialchar("Hello, World?"), "Hello:World:?")
        self.assertEqual(replace_specialchar("Hello, World;"), "Hello:World:;")
        self.assertEqual(replace_specialchar("Hello, World()"), "Hello:World:()")
        self.assertEqual(replace_specialchar("Hello, World[]"), "Hello:World:[]")
        self.assertEqual(replace_specialchar("Hello, World{}"), "Hello:World:{}")
