import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialChar(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_max_specialchar("hello, world", 1), "hello: world")

    def test_boundary_conditions(self):
        self.assertEqual(replace_max_specialchar("", 1), "")
        self.assertEqual(replace_max_specialchar("no_special_chars", 1), "no_special_chars")
        self.assertEqual(replace_max_specialchar("one.two,three", 0), "one.two,three")
        self.assertEqual(replace_max_specialchar("one.two,three", 3), "one:two:three")

    def test_complex_cases(self):
        self.assertEqual(replace_max_specialchar("one,two.three,four", 2), "one:two:three,four")
        self.assertEqual(replace_max_specialchar("one,two.three,four", 3), "one:two:three:four")
        self.assertEqual(replace_max_specialchar("one,two.three,four", 4), "one:two:three:four")
