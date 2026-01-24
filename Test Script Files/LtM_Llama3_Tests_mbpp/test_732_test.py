import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")
        self.assertEqual(replace_specialchar("This is a test."), "This: is: a: test:")
        self.assertEqual(replace_specialchar("A, B, C"), "A:, B:, C:")

    def test_edge_cases(self):
        self.assertEqual(replace_specialchar(""), "")
        self.assertEqual(replace_specialchar(":"), ":")
        self.assertEqual(replace_specialchar("a"), "a")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_specialchar(123)
        with self.assertRaises(TypeError):
            replace_specialchar([1, 2, 3])
