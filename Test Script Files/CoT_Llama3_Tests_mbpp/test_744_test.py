import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_none((1, None, 3, None, 5)))

    def test_no_none(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_all_none(self):
        self.assertTrue(check_none((None, None, None)))

    def test_empty_tuple(self):
        self.assertFalse(check_none(()))

    def test_single_element(self):
        self.assertFalse(check_none((1,)))

    def test_multiple_none(self):
        self.assertTrue(check_none((None, None, None, None)))

    def test_mixed_elements(self):
        self.assertTrue(check_none((1, None, 3, None, 5)))

    def test_mixed_elements_with_empty(self):
        self.assertTrue(check_none((1, None, 3, None, 5, None)))
