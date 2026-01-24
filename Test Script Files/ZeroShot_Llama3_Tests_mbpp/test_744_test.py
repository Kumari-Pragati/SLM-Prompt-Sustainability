import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_check_none(self):
        self.assertTrue(check_none((1, 2, 3)))
        self.assertFalse(check_none((1, 2, None)))
        self.assertTrue(check_none((1, None, 3)))
        self.assertTrue(check_none((None, 2, 3)))
        self.assertTrue(check_none((None, None, 3)))
        self.assertFalse(check_none((1, 2, 3, 4)))
        self.assertFalse(check_none((1, 2, 3, None)))
        self.assertTrue(check_none((1, 2, None, 4)))
        self.assertTrue(check_none((None, 2, None, 3)))
        self.assertTrue(check_none((None, None, None, 3)))
        self.assertTrue(check_none((None, None, None, None)))
        self.assertFalse(check_none((1, 2, 3, 4, 5)))
