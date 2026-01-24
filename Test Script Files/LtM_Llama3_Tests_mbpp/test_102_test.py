import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")
        self.assertEqual(snake_to_camel("abc"), "Abc")
        self.assertEqual(snake_to_camel("snake_to_camel"), "SnakeToCamel")

    def test_edge(self):
        self.assertEqual(snake_to_camel(""), "")
        self.assertEqual(snake_to_camel("_"), "_")
        self.assertEqual(snake_to_camel("snake_to_camel_"), "SnakeToCamel")

    def test_invalid(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)
        with self.assertRaises(TypeError):
            snake_to_camel(None)
