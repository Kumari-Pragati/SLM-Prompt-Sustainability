import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_extract_values(self):
        self.assertEqual(extract_values('"hello" "world"'), ['hello', 'world'])
        self.assertEqual(extract_values('"foo" "bar" "baz"'), ['foo', 'bar', 'baz'])
        self.assertEqual(extract_values('"one" "two" "three" "four"'), ['one', 'two', 'three', 'four'])
        self.assertEqual(extract_values('"5" "10" "15"'), ['5', '10', '15'])
        self.assertEqual(extract_values('"apple" "banana" "cherry"'), ['apple', 'banana', 'cherry'])
