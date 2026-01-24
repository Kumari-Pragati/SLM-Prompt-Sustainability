import unittest
from mbpp_411_code import snake_to_camel

class TestSnakeToCamel(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(snake_to_camel('simple_case'), 'SimpleCase')
        self.assertEqual(snake_to_camel('another_simple_case'), 'AnotherSimpleCase')

    def test_edge_cases(self):
        self.assertEqual(snake_to_camel(''), '')
        self.assertEqual(snake_to_camel('_only_underscores'), 'OnlyUnderscores')
        self.assertEqual(snake_to_camel('no_change_needed'), 'NoChangeNeeded')

    def test_complex_cases(self):
        self.assertEqual(snake_to_camel('complex_case_with_numbers_123'), 'ComplexCaseWithNumbers123')
        self.assertEqual(snake_to_camel('CAPS_AND_SMALLS'), 'CapsAndSmalls')
