import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_max("12345"), 5)

    def test_edge_condition(self):
        self.assertEqual(extract_max(""), None)

    def test_boundary_condition(self):
        self.assertEqual(extract_max("1"), 1)

    def test_multiple_numbers(self):
        self.assertEqual(extract_max("1234567890"), 9)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            extract_max(12345)
