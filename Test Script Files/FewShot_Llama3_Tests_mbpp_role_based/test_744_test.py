import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertFalse(check_none(()))

    def test_all_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_mixed_values(self):
        self.assertTrue(check_none((1, None, 3)))

    def test_no_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_single_none(self):
        self.assertTrue(check_none((1, None, 3)))

    def test_tuple_with_one_none(self):
        self.assertTrue(check_none((1, None, 2)))

    def test_tuple_with_two_none(self):
        self.assertTrue(check_none((1, None, None)))

    def test_tuple_with_three_none(self):
        self.assertTrue(check_none((None, None, None)))
