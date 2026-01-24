import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_end_num_with_numbers(self):
        self.assertTrue(end_num('abc1'))
        self.assertTrue(end_num('123'))
        self.assertTrue(end_num('abc123'))

    def test_end_num_without_numbers(self):
        self.assertFalse(end_num('abc'))
        self.assertFalse(end_num(''))

    def test_end_num_with_special_characters(self):
        self.assertTrue(end_num('abc@1'))
        self.assertTrue(end_num('abc@123'))

    def test_end_num_with_whitespace(self):
        self.assertFalse(end_num('abc 1'))
        self.assertFalse(end_num('abc 123'))

    def test_end_num_with_mixed_case(self):
        self.assertTrue(end_num('Abc1'))
        self.assertTrue(end_num('ABC123'))

    def test_end_num_with_numbers_at_beginning(self):
        self.assertFalse(end_num('1abc'))
        self.assertFalse(end_num('123abc'))

    def test_end_num_with_numbers_at_end(self):
        self.assertTrue(end_num('abc1'))
        self.assertTrue(end_num('abc123'))

    def test_end_num_with_numbers_and_special_characters(self):
        self.assertTrue(end_num('abc@1'))
        self.assertTrue(end_num('abc@123'))

    def test_end_num_with_numbers_and_whitespace(self):
        self.assertFalse(end_num('abc 1'))
        self.assertFalse(end_num('abc 123'))
