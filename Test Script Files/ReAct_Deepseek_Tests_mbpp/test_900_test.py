import unittest
from mbpp_900_code import match_num

class TestMatchNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(match_num("5"))
        self.assertTrue(match_num("5678"))

    def test_edge_cases(self):
        self.assertFalse(match_num(""))
        self.assertFalse(match_num("4"))
        self.assertFalse(match_num("678"))

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(match_num(None))
        self.assertFalse(match_num(1234))
        self.assertFalse(match_num(True))
        self.assertFalse(match_num([5]))
