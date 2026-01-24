import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_typical(self):
        self.assertTrue(check_none((None, 1, 2, 3)))
        self.assertFalse(check_none((1, 2, 3)))

    def test_edge(self):
        self.assertTrue(check_none((None, None, 1, 2)))
        self.assertFalse(check_none((1, 2, 3)))

    def test_corner(self):
        self.assertTrue(check_none((None, 1, None, 2)))
        self.assertFalse(check_none((1, 2, 3)))

    def test_empty(self):
        self.assertFalse(check_none(()))

    def test_single(self):
        self.assertFalse(check_none((1,)))

    def test_all_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_mixed(self):
        self.assertTrue(check_none((None, 1, None, 2)))
