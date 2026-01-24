import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(extract_max("123"), 123)
        self.assertEqual(extract_max("4567"), 67)
        self.assertEqual(extract_max("987654"), 987654)

    def test_edge_cases(self):
        self.assertEqual(extract_max("0"), 0)
        self.assertEqual(extract_max("1"), 1)
        self.assertEqual(extract_max("9"), 9)
        self.assertEqual(extract_max("1234567890"), 1234567890)
        self.assertEqual(extract_max("12345678901"), 1234567890)

    def test_multiple_numbers(self):
        self.assertEqual(extract_max("123 456 789"), 789)
        self.assertEqual(extract_max("12345678901234567890"), 12345678901234567890)

    def test_no_numbers(self):
        self.assertEqual(extract_max("abc"), None)
        self.assertEqual(extract_max("123a"), None)
        self.assertEqual(extract_max("a123"), None)
