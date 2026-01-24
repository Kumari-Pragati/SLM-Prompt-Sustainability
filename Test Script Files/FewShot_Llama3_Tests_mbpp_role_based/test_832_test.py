import unittest
from mbpp_832_code import extract_max

class TestExtractMax(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_max("Hello, my phone number is 1234567890. Goodbye!"), 9876543210)

    def test_multiple_numbers(self):
        self.assertEqual(extract_max("I have 3 dogs: 1, 2, 3. I also have 4 cats: 10, 20, 30, 40.")), 40)

    def test_single_number(self):
        self.assertEqual(extract_max("My favorite number is 42.")), 42)

    def test_empty_input(self):
        self.assertIsNone(extract_max(""))

    def test_non_numeric_input(self):
        self.assertIsNone(extract_max("Hello, world!"))

    def test_no_numbers(self):
        self.assertIsNone(extract_max("This is a sentence with no numbers."))
