import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_match_num_true(self):
        self.assertTrue(match_num('5'))
        self.assertTrue(match_num('5678'))
        self.assertTrue(match_num('50'))
        self.assertTrue(match_num('55555'))

    def test_match_num_false(self):
        self.assertFalse(match_num(''))
        self.assertFalse(match_num('abc'))
        self.assertFalse(match_num('123'))
        self.assertFalse(match_num('456'))
        self.assertFalse(match_num('789'))
        self.assertFalse(match_num('56789'))
        self.assertFalse(match_num('05'))
