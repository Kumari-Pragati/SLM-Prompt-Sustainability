import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')
        self.assertEqual(snake_to_camel('python_programming'), 'PythonProgramming')
        self.assertEqual(snake_to_camel('simple_case'), 'SimpleCase')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel('_hello_world'), '_HelloWorld')
        self.assertEqual(snake_to_camel('hello_world_'), 'HelloWorld_')
        self.assertEqual(snake_to_camel('__hello_world__'), '__HelloWorld__')

    def test_corner_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('____'), '____')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            snake_to_camel(1234)
        with self.assertRaises(TypeError):
            snake_to_camel(['hello_world'])
        with self.assertRaises(TypeError):
            snake_to_camel({'hello_world': 'HelloWorld'})
