import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('single'), 'single')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'allcaps')

    def test_number_in_middle(self):
        self.assertEqual(camel_to_snake('camel2Snake'), 'camel2_snake')

    def test_number_at_end(self):
        self.assertEqual(camel_to_snake('camelToSnake1'), 'camel_to_snake1')

    def test_special_characters(self):
        self.assertEqual(camel_to_snake('camel@ToSnake'), 'camel_to_snake')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)
