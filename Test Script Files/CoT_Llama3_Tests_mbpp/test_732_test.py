import unittest
from mbpp_732_code import replace_specialchar

class TestReplaceSpecialchar(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(replace_specialchar("Hello, world!"), "Hello:, world:")
        self.assertEqual(replace_specialchar("This is a test. 123"), "This:, is:, a:, test.: 123:")

    def test_edge_cases(self):
        self.assertEqual(replace_specialchar(""), "")
        self.assertEqual(replace_specialchar("Hello"), "Hello")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            replace_specialchar(None)
        with self.assertRaises(TypeError):
            replace_specialchar(123)

    def test_boundary_conditions(self):
        self.assertEqual(replace_specialchar(".,"), "::")
        self.assertEqual(replace_specialchar(","), "::")
