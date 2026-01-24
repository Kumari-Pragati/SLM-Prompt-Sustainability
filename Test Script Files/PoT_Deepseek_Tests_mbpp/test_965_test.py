import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')
        self.assertEqual(camel_to_snake('convertHTMLToMarkdown'), 'convert_html_to_markdown')

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(''), '')
        self.assertEqual(camel_to_snake('a'), 'a')
        self.assertEqual(camel_to_snake('A'), 'a')
        self.assertEqual(camel_to_snake('123'), '123')

    def test_corner_cases(self):
        self.assertEqual(camel_to_snake('camelCase'), 'camel_case')
        self.assertEqual(camel_to_snake('PascalCase'), 'pascal_case')
        self.assertEqual(camel_to_snake('snake_case'), 'snake_case')
        self.assertEqual(camel_to_snake('UPPERCASE'), 'uppercase')
        self.assertEqual(camel_to_snake('lowercase'), 'lowercase')
