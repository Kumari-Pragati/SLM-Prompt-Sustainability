import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(find_char("HelloWorld"), ["Hello", "World"])
        self.assertListEqual(find_char("Python3.9"), ["Python", "3.9"])
        self.assertListEqual(find_char("JavaScriptES6"), ["JavaScript", "ES6"])

    def test_edge_case_short(self):
        self.assertListEqual(find_char("AbC"), ["AbC"])
        self.assertListEqual(find_char("123"), [])
        self.assertListEqual(find_char("_"), [])
        self.assertListEqual(find_char(" "), [])

    def test_edge_case_long(self):
        self.assertListEqual(find_char("AaBbCcDdEeFfGgHhIiJj"), ["AaBbCcDdEeFfGgHhIiJj"])
        self.assertListEqual(find_char("ZzYyXxWwVvUuTtSsRrQqPpOoNnMmLlKkJjIiHhGgFfEeDdCcBbAa"), ["AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"])

    def test_corner_case_empty(self):
        self.assertListEqual(find_char(""), [])
