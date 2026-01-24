import unittest
from mbpp_933_code import camel_to_snake

class TestCamelToSnake(unittest.TestCase):

    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("camelCase"), "camel_case")
        self.assertEqual(camel_to_snake("CamelCase"), "camel_case")
        self.assertEqual(camel_to_snake("camelCase123"), "camel_case123")
        self.assertEqual(camel_to_snake("camelCase123ABC"), "camel_case123_abc")
        self.assertEqual(camel_to_snake("camelCase123ABC456"), "camel_case123_abc456")
        self.assertEqual(camel_to_snake("camelCase123ABC456789"), "camel_case123_abc456789")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890"), "camel_case123_abc4567890")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_"), "camel_case123_abc4567890_")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc"), "camel_case123_abc4567890_abc")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123"), "camel_case123_abc4567890_abc123")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC"), "camel_case123_abc4567890_abc123_abc")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC456"), "camel_case123_abc4567890_abc123_abc456")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC456789"), "camel_case123_abc4567890_abc123_abc456789")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890"), "camel_case123_abc4567890_abc123_abc4567890")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_"), "camel_case123_abc4567890_abc123_abc4567890_")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc"), "camel_case123_abc4567890_abc123_abc4567890_abc")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123"), "camel_case123_abc4567890_abc123_abc4567890_abc123")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC456"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc456")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC456789"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc456789")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC4567890"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc4567890")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC4567890_"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc4567890_")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC4567890_abc"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc4567890_abc")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC4567890_abc123"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc4567890_abc123")
        self.assertEqual(camel_to_snake("camelCase123ABC4567890_abc123ABC4567890_abc123ABC4567890_abc123ABC"), "camel_case123_abc4567890_abc123_abc4567890_abc123_abc