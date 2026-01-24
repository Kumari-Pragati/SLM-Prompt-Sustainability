import unittest
from mbpp_204_code import count

class TestCountFunction(unittest.TestCase):

    def test_count_with_valid_input(self):
        self.assertEqual(count('abcabc', 'a'), 2)
        self.assertEqual(count('abcabc', 'b'), 2)
        self.assertEqual(count('abcabc', 'c'), 2)
        self.assertEqual(count('aaaaaa', 'a'), 6)
        self.assertEqual(count('abcabc', 'd'), 0)

    def test_count_with_empty_string(self):
        self.assertEqual(count('', 'a'), 0)
        self.assertEqual(count('', 'b'), 0)
        self.assertEqual(count('', 'c'), 0)

    def test_count_with_special_characters(self):
        self.assertEqual(count('!@#$%^&*', '#'), 1)
        self.assertEqual(count('!@#$%^&*', '%'), 1)
        self.assertEqual(count('!@#$%^&*', '&'), 1)
        self.assertEqual(count('!@#$%^&*', '('), 0)

    def test_count_with_numbers(self):
        self.assertEqual(count('1234567890', '1'), 1)
        self.assertEqual(count('1234567890', '2'), 1)
        self.assertEqual(count('1234567890', '3'), 1)
        self.assertEqual(count('1234567890', '0'), 1)
        self.assertEqual(count('1234567890', '5'), 0)
