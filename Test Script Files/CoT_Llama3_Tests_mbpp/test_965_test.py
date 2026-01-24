import unittest
from mbpp_965_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("testFunction"), "test_function")

    def test_edge_cases(self):
        self.assertEqual(camel_to_snake(""), "")
        self.assertEqual(camel_to_snake("test"), "test")
        self.assertEqual(camel_to_snake("Test"), "test")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            camel_to_snake(123)
        with self.assertRaises(TypeError):
            camel_to_snake(None)

    def test_boundary_cases(self):
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")
        self.assertEqual(camel_to_snake("ALLCAPS"), "allcaps")
        self.assertEqual(camel_to_snake("123456"), "123456")
