import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(check_none((None, 1, 2)))

    def test_simple_false(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_empty_input(self):
        self.assertFalse(check_none(()))

    def test_all_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_mixed_none(self):
        self.assertTrue(check_none((None, 1, None)))

    def test_all_non_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_single_none(self):
        self.assertTrue(check_none((1, None, 3)))

    def test_multiple_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_none_at_end(self):
        self.assertTrue(check_none((1, 2, None)))

    def test_none_at_start(self):
        self.assertTrue(check_none((None, 2, 3)))

    def test_none_in_middle(self):
        self.assertTrue(check_none((1, None, 3)))
