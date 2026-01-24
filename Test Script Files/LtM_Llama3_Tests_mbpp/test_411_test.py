import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_simple_snake_to_camel(self):
        self.assertEqual(snake_to_camel('hello_world'), 'HelloWorld')
        self.assertEqual(snake_to_camel('test_case'), 'TestCase')
        self.assertEqual(snake_to_camel('snake_to_camel'), 'SnakeToCamel')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('snake'),'snake')

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            snake_to_camel(123)
        with self.assertRaises(TypeError):
            snake_to_camel(None)
        with self.assertRaises(TypeError):
            snake_to_camel('')
