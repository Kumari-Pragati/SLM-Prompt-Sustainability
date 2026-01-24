import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')
        self.assertEqual(snake_to_camel('python_programming'), 'PythonProgramming')
        self.assertEqual(snake_to_camel('test_case'), 'TestCase')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel('_hello_world'), '_HelloWorld')
        self.assertEqual(snake_to_camel('hello_world_'), 'HelloWorld_')
        self.assertEqual(snake_to_camel('_hello_world_'), '_HelloWorld_')

    def test_corner_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('____'), '____')
