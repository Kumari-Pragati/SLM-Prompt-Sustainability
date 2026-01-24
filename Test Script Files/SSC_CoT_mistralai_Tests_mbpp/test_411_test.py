import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(snake_to_camel('some_variable_name'), 'someVariableName')
        self.assertEqual(snake_to_camel('single_word'), 'singleWord')
        self.assertEqual(snake_to_camel('multi_word'), 'multiWord')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_'), '_')
        self.assertEqual(snake_to_camel('__'), '__')
        self.assertEqual(snake_to_camel('_single_word'), 'SingleWord')
        self.assertEqual(snake_to_camel('single_word_'), 'SingleWord')
        self.assertEqual(snake_to_camel('_singleWord_'), 'SingleWord')

    def test_boundary_cases(self):
        self.assertEqual(snake_to_camel('long_variable_name_with_many_underscores'), 'longVariableNameWithManyUnderscores')
        self.assertEqual(snake_to_camel('long_variable_name_with_one_underscore'), 'longVariableNameWithOneUnderscore')
        self.assertEqual(snake_to_camel('long_variable_name_with_two_underscores'), 'longVariableNameWithTwoUnderscores')
