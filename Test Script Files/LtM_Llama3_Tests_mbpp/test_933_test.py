import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("test"), "test")
        self.assertEqual(camel_to_snake("abc"), "abc")

    def test_edge(self):
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("a"), "a")
        self.assertEqual(camel_to_snake("A"), "a")
        self.assertEqual(camel_to_snake("123"), "123")

    def test_complex(self):
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")
        self.assertEqual(camel_to_snake("CamelCaseIsFun"), "camel_case_is_fun")
        self.assertEqual(camel_to_snake("CamelCaseIsNotFun"), "camel_case_is_not_fun")
