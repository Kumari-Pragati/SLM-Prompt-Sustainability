import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')
        self.assertEqual(snake_to_camel('python_programming'), 'PythonProgramming')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel('_hello_world'), '_HelloWorld')
        self.assertEqual(snake_to_camel('hello_world_'), 'HelloWorld_')

    def test_corner_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('____'), '____')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            snake_to_camel(1234)
        with self.assertRaises(TypeError):
            snake_to_camel(['hello', 'world'])
