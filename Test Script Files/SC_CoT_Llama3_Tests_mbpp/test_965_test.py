import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")

    def test_edge_case(self):
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")

    def test_boundary_case(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_multiple_words(self):
        self.assertEqual(camel_to_snake("helloWorldThisIsATest"), "hello_world_this_is_a_test")

    def test_uppercase_only(self):
        self.assertEqual(camel_to_snake("HELLO"), "hello")

    def test_lowercase_only(self):
        self.assertEqual(camel_to_snake("hello"), "hello")

    def test_mixed_case(self):
        self.assertEqual(camel_to_snake("helloWorldThisIsATest"), "hello_world_this_is_a_test")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)

    def test_empty_string(self):
        self.assertEqual(camel_to_snake(""), "")
