import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_check_none_with_none(self):
        self.assertTrue(check_none((None, 1, 2, 3)))
        self.assertTrue(check_none((1, 2, 3, None)))
        self.assertTrue(check_none((1, None, 2, 3)))
        self.assertTrue(check_none((1, 2, None, 3)))
        self.assertTrue(check_none((1, 2, 3, None)))

    def test_check_none_without_none(self):
        self.assertFalse(check_none((1, 2, 3)))
        self.assertFalse(check_none(()))

    def test_check_none_with_empty_tuple(self):
        self.assertFalse(check_none(()))
