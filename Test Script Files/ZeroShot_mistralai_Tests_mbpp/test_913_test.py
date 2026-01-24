import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):

    def test_end_num_with_number(self):
        self.assertTrue(end_num("Hello123"))
        self.assertTrue(end_num("123"))
        self.assertTrue(end_num("abcd123"))
        self.assertTrue(end_num("123xyz"))

    def test_end_num_without_number(self):
        self.assertFalse(end_num("Hello"))
        self.assertFalse(end_num("abcd"))
        self.assertFalse(end_num("abcdEFG"))
        self.assertFalse(end_num("123_"))
