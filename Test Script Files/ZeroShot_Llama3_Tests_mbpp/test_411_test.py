import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("hello_world123"), "helloWorld123")
        self.assertEqual(snake_to_camel("hello"), "hello")
        self.assertEqual(snake_to_camel("hello_world_abc"), "helloWorld_abc")
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel("abc_def"), "abcDef")
        self.assertEqual(snake_to_camel("hello_world_abc_def"), "helloWorld_abcDef")

    def test_snake_to_camel_edge_cases(self):
        self.assertEqual(snake_to_camel("_hello"), "_hello")
        self.assertEqual(snake_to_camel("hello_"), "hello")
        self.assertEqual(snake_to_camel("_hello_"), "_hello")
        self.assertEqual(snake_to_camel("hello__world"), "helloWorld")
