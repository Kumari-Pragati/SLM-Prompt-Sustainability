import unittest
from mbpp_102_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(snake_to_camel('some_variable_name'), 'someVariableName')
        self.assertEqual(snake_to_camel('another_variable_name'), 'anotherVariableName')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('__'), '__')
        self.assertEqual(snake_to_camel('_variable'), 'Variable')
        self.assertEqual(snake_to_camel('variable_'), 'Variable')
        self.assertEqual(snake_to_camel('variable__'), 'Variable')

    def test_boundary_cases(self):
        self.assertEqual(snake_to_camel('short_word'), 'shortWord')
        self.assertEqual(snake_to_camel('long_variable_name'), 'longVariableName')
        self.assertEqual(snake_to_camel('longest_variable_name_in_the_universe'), 'longestVariableNameInTheUniverse')

    def test_invalid_inputs(self):
        self.assertEqual(snake_to_camel(123), '')
        self.assertEqual(snake_to_camel(None), '')
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel(' '), ' ')
