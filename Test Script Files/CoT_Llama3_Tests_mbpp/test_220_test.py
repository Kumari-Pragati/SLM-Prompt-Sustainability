import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialchar(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(replace_max_specialchar("Hello, world!", 1), "Hello:, world!")
        self.assertEqual(replace_max_specialchar("This is a test, with multiple commas", 2), "This is a test:, with multiple :,")
        self.assertEqual(replace_max_specialchar("This is a test, with multiple spaces", 1), "This is a test:, with multiple spaces")

    def test_edge_cases(self):
        self.assertEqual(replace_max_specialchar("", 0), "")
        self.assertEqual(replace_max_specialchar("a", 0), "a")
        self.assertEqual(replace_max_specialchar("a", 1), "a")
        self.assertEqual(replace_max_specialchar("a", 2), "a")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_max_specialchar(123, 1)
        with self.assertRaises(TypeError):
            replace_max_specialchar("Hello, world!", "a")
        with self.assertRaises(TypeError):
            replace_max_specialchar(None, 1)
