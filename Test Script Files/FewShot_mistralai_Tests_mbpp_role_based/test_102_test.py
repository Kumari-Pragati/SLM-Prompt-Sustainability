import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(snake_to_camel('snake_case'), 'snakeCase')
        self.assertEqual(snake_to_camel('camelCase'), 'camelCase')
        self.assertEqual(snake_to_camel('mixedCase'), 'mixedCase')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('__'), '__')
        self.assertEqual(snake_to_camel('_word'), 'Word')
        self.assertEqual(snake_to_camel('word_'), 'Word')
        self.assertEqual(snake_to_camel('word_1'), 'Word1')
        self.assertEqual(snake_to_camel('1_word'), '1Word')
        self.assertEqual(snake_to_camel('word_123'), 'Word123')
        self.assertEqual(snake_to_camel('123_word'), '123Word')
