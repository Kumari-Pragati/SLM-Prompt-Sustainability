import unittest
from mbpp_220_code import replace_max_specialchar

class TestReplaceMaxSpecialChar(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello:World!")

    def test_edge_case_n_equals_zero(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 0), "Hello, World!")

    def test_boundary_case_n_equals_one(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello:World!")

    def test_boundary_case_n_equals_two(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 2), "Hello::World!")

    def test_corner_case_no_special_char(self):
        self.assertEqual(replace_max_specialchar("HelloWorld", 2), "HelloWorld")

    def test_corner_case_all_special_chars(self):
        self.assertEqual(replace_max_specialchar(",.", 2), "::")

    def test_corner_case_more_special_chars_than_n(self):
        self.assertEqual(replace_max_specialchar("Hello, World!", 1), "Hello:World!")

    def test_corner_case_special_chars_at_end(self):
        self.assertEqual(replace_max_specialchar("Hello, World. Nice, day!", 2), "Hello:World. Nice, day!")
