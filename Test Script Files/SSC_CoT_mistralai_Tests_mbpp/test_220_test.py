import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 3), "Hello:World:")
        self.assertEqual(replace_max_specialchar("Python is awesome!", 2), "Python:is:awesome:")

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(replace_max_specialchar("", 3), "")
        self.assertEqual(replace_max_specialchar("Hello, World!", 0), "Hello, World!")
        self.assertEqual(replace_max_specialchar("Hello, World!", 4), "Hello:World:")
        self.assertEqual(replace_max_specialchar("Hello, World!", 5), "Hello:World:")

    def test_special_characters(self):
        self.assertEqual(replace_max_specialchar("Hello, World!@#$%^&*()_+-=", 3), "Hello:World!@#$:")
        self.assertEqual(replace_max_specialchar("Hello, World!@#$%^&*()_+-=", 4), "Hello:World!@#$:")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar(123, 3)
        with self.assertRaises(TypeError):
            replace_max_specialchar(None, 3)
