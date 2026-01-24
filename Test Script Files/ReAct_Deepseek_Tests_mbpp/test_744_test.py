import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):

    def test_typical_case_with_none(self):
        self.assertTrue(check_none((1, 2, None, 4)))

    def test_typical_case_without_none(self):
        self.assertFalse(check_none((1, 2, 3, 4)))

    def test_empty_tuple(self):
        self.assertFalse(check_none(()))

    def test_tuple_with_only_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_single_element_tuple_with_none(self):
        self.assertTrue(check_none((None,)))

    def test_single_element_tuple_without_none(self):
        self.assertFalse(check_none((1,)))

    def test_tuple_with_mixed_types(self):
        self.assertTrue(check_none((1, 'two', None, 4.0)))
