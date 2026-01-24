import unittest
from mbpp_862_code import n_common_words

class TestNCommonWords(unittest.TestCase):

    def test_typical_case(self):
        text = "Hello world, world is beautiful"
        n = 2
        expected_output = [('world', 2), ('Hello', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_edge_case(self):
        text = "Hello world, world is beautiful"
        n = 10
        self.assertEqual(len(n_common_words(text, n)), 5)

    def test_corner_case(self):
        text = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
        n = 1
        expected_output = [('A', 1)]
        self.assertEqual(n_common_words(text, n), expected_output)

    def test_invalid_input(self):
        text = "Hello world, world is beautiful"
        n = -1
        with self.assertRaises(ValueError):
            n_common_words(text, n)
