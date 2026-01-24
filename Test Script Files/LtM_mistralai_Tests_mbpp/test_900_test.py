import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):
    def test_simple_match(self):
        self.assertTrue(match_num("5"))
        self.assertTrue(match_num("05"))
        self.assertTrue(match_num("5.0"))

    def test_non_match(self):
        self.assertFalse(match_num("6"))
        self.assertFalse(match_num("5a"))
        self.assertFalse(match_num("5_"))
        self.assertFalse(match_num("5 "))
        self.assertFalse(match_num("5\t"))
        self.assertFalse(match_num("5\n"))
        self.assertFalse(match_num("5.6"))
        self.assertFalse(match_num("5+"))
        self.assertFalse(match_num("5-"))
        self.assertFalse(match_num("5["))
        self.assertFalse(match_num("5]"))
        self.assertFalse(match_num("5("))
        self.assertFalse(match_num("5)"))
        self.assertFalse(match_num("5{"))
        self.assertFalse(match_num("5}"))
        self.assertFalse(match_num("5|"))
        self.assertFalse(match_num("5\ "))
        self.assertFalse(match_num(""))
        self.assertFalse(match_num(None))
