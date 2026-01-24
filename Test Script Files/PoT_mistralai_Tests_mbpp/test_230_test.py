import unittest
from mbpp_230_code import replace_blank

class TestReplaceBlank(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(replace_blank("Hello World", "X"), "Hello Xorld")

    def test_edge_case_empty_string(self):
        self.assertEqual(replace_blank("", "X"), "")

    def test_edge_case_single_space(self):
        self.assertEqual(replace_blank(" ", "X"), "X")

    def test_edge_case_single_char(self):
        self.assertEqual(replace_blank("a", "X"), "a")

    def test_boundary_case_long_string(self):
        self.assertEqual(replace_blank("Hello World Hello World" * 10, "X"), "Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld Hello Xorld")
