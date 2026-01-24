import unittest
from mbpp_563_code import extract_values

class TestExtractValues(unittest.TestCase):

    def test_simple(self):
        self.assertListEqual(extract_values('"value1" "value2"'), ['value1', 'value2'])
        self.assertListEqual(extract_values('"value"'), ['value'])
        self.assertListEqual(extract_values('"value1" "value2" "value3"'), ['value1', 'value2', 'value3'])

    def test_edge_and_boundary(self):
        self.assertListEqual(extract_values('"value" " "'), ['value'])
        self.assertListEqual(extract_values('" "'), [])
        self.assertListEqual(extract_values('"value" "value"'), ['value'])
        self.assertListEqual(extract_values('"value" "value" "value"'), ['value'])
        self.assertListEqual(extract_values('"value" "value" "value" "value"'), ['value'])

    def test_complex(self):
        self.assertListEqual(extract_values('"value1" "value2" "value3" "value4" "value5"'), ['value1', 'value2', 'value3', 'value4', 'value5'])
        self.assertListEqual(extract_values('"value1" "value2" "value3" "value4" "value5" "value6"'), ['value1', 'value2', 'value3', 'value4', 'value5', 'value6'])
        self.assertListEqual(extract_values('"value1" "value2" "value3" "value4" "value5" "value6" "value7"'), ['value1', 'value2', 'value3', 'value4', 'value5', 'value6', 'value7'])
