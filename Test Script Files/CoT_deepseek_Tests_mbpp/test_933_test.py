import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(camel_to_snake('camelToSnake'), 'camel_to_snake')

    def test_single_word(self):
        self.assertEqual(camel_to_snake('snake'), 'snake')

    def test_already_snake_case(self):
        self.assertEqual(camel_to_snake('already_snake_case'), 'already_snake_case')

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(''), '')

    def test_all_caps(self):
        self.assertEqual(camel_to_snake('ALLCAPS'), 'allcaps')

    def test_number_in_middle(self):
        self.assertEqual(camel_to_snake('camel1ToSnake'), 'camel1_to_snake')

    def test_number_at_end(self):
        self.assertEqual(camel_to_snake('camelToSnake2'), 'camel_to_snake2')

    def test_special_characters(self):
        self.assertEqual(camel_to_snake('camelTo@Snake'), 'camel_to_@_snake')

    def test_special_characters_at_end(self):
        self.assertEqual(camel_to_snake('camelToSnake@'), 'camel_to_snake@')

    def test_special_characters_at_start(self):
        self.assertEqual(camel_to_snake('@camelToSnake'), '_camel_to_snake')

    def test_special_characters_in_middle(self):
        self.assertEqual(camel_to_snake('c@melToSnake'), 'c_@_mel_to_snake')
