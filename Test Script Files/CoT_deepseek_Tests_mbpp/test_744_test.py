import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_none((1, None, 3)))

    def test_no_none_case(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_empty_tuple(self):
        self.assertFalse(check_none(()))

    def test_single_none(self):
        self.assertTrue(check_none((None,)))

    def test_all_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_mixed_types(self):
        self.assertTrue(check_none((1, None, 'a')))

    def test_none_as_string(self):
        self.assertFalse(check_none(('None', 2, 3)))

    def test_none_as_integer(self):
        self.assertFalse(check_none((1, 2, 3), 0))

    def test_none_as_float(self):
        self.assertFalse(check_none((1.0, 2.0, 3.0)))

    def test_none_as_boolean(self):
        self.assertFalse(check_none((True, False, True)))
