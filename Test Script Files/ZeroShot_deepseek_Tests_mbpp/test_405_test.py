import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_check_tuplex_positive(self):
        self.assertTrue(check_tuplex(('a', 'b', 'c'), ('a', 'b')))
        self.assertTrue(check_tuplex((1, 2, 3), (2, 3)))
        self.assertTrue(check_tuplex((True, False), (True,)))

    def test_check_tuplex_negative(self):
        self.assertFalse(check_tuplex(('a', 'b', 'c'), ('d', 'e')))
        self.assertFalse(check_tuplex((1, 2, 3), (4, 5)))
        self.assertFalse(check_tuplex((True, False), (False, True)))
