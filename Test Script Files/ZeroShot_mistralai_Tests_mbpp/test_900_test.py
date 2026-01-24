import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_match_num_with_five(self):
        self.assertTrue(match_num("5"))

    def test_match_num_with_not_five(self):
        self.assertFalse(match_num("4"))
        self.assertFalse(match_num("6"))
        self.assertFalse(match_num("5a"))
        self.assertFalse(match_num("5_"))
