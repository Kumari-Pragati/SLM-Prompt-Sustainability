import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(find_char("HelloWorld"), ["Hello", "World"])
        self.assertListEqual(find_char("PythonProgramming"), ["Python", "Programming"])

    def test_edge_cases(self):
        self.assertListEqual(find_char("Aaa"), ["Aaa"])
        self.assertListEqual(find_char("AaaBbbCcc"), ["Aaa", "Bbb", "Ccc"])
        self.assertListEqual(find_char("AaaBbbCccDdd"), ["Aaa", "Bbb", "Ccc", "Ddd"])
        self.assertListEqual(find_char("AaaBbbCccDddEee"), ["Aaa", "Bbb", "Ccc", "Ddd", "Eee"])

    def test_boundary_conditions(self):
        self.assertListEqual(find_char("AaaBbbCcc"), ["Aaa", "Bbb", "Ccc"])
        self.assertListEqual(find_char("AaaBbbCccD"), ["Aaa", "Bbb", "Ccc"])
        self.assertListEqual(find_char("AaaBbbCccDdd"), ["Aaa", "Bbb", "Ccc", "Ddd"])
        self.assertListEqual(find_char("AaaBbbCccDddE"), ["Aaa", "Bbb", "Ccc", "Ddd", "E"])

    def test_invalid_input(self):
        self.assertListEqual(find_char(""), [])
        self.assertListEqual(find_char(None), [])
        self.assertListEqual(find_char("123"), [])
        self.assertListEqual(find_char("12345"), [])
        self.assertListEqual(find_char("123456"), [])
        self.assertListEqual(find_char("1234567"), [])
        self.assertListEqual(find_char("12345678"), [])
        self.assertListEqual(find_char("123456789"), [])
        self.assertListEqual(find_char("1234567890"), [])
