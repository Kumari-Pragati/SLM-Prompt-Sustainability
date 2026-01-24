import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertFalse(check_none(()))

    def test_all_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_mixed_values(self):
        self.assertTrue(check_none((None, 1, None, "hello", None)))

    def test_no_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_single_none(self):
        self.assertTrue(check_none((1, None, 3)))

    def test_tuple_with_none_and_non_none(self):
        self.assertTrue(check_none((1, None, "hello", None, 3)))

    def test_tuple_with_multiple_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_tuple_with_multiple_non_none(self):
        self.assertFalse(check_none((1, 2, 3)))
