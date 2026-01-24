import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")

    def test_edge_case(self):
        self.assertEqual(capital_words_spaces("A"), "A")

    def test_boundary_case(self):
        self.assertEqual(capital_words_spaces("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            capital_words_spaces(123)
