import unittest
from mbpp_877_code import sort_String

class TestSortString(unittest.TestCase):
    def test_sort_string_normal(self):
        self.assertEqual(sort_String("HelloWorld"), "alhElloOorrdW")
        self.assertEqual(sort_String("Python"), "hPythonn")
        self.assertEqual(sort_String("12345"), "12345")
        self.assertEqual(sort_String("aBcDeFgHiJkLmNoPqRsTuVwXyZ"), "aAaBbBbCcCcDdDdEeEeFfFfGgGgHhHhIiIiJjJjKkKkLlLlMmMmNnNnOoOoPpPpQqQqRrRrSsSsTtTtUuUuVvVvWwWwXxXxYyYyZzZz")

    def test_sort_string_empty(self):
        self.assertEqual(sort_String(""), "")

    def test_sort_string_single_char(self):
        for char in "!@#$%^&*()_+-=[]{};:'\",.<>?/":
            self.assertEqual(sort_String(char), char)

    def test_sort_string_special_case(self):
        self.assertEqual(sort_String("1A"), "1A")
        self.assertEqual(sort_String("A1"), "A1")
        self.assertEqual(sort_String("1A1"), "1A1")
        self.assertEqual(sort_String("A1A"), "A1A")
