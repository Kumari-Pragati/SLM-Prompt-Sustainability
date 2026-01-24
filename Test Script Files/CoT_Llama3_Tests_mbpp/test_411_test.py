import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(snake_to_camel("hello_world"), "HelloWorld")

    def test_edge_case(self):
        self.assertEqual(snake_to_camel("hello"), "hello")

    def test_edge_case2(self):
        self.assertEqual(snake_to_camel("hello_world123"), "HelloWorld123")

    def test_edge_case3(self):
        self.assertEqual(snake_to_camel("_hello_world"), "_helloWorld")

    def test_edge_case4(self):
        self.assertEqual(snake_to_camel("hello_world_"), "HelloWorld_")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            snake_to_camel(None)
