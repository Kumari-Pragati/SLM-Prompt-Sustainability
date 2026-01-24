import unittest
from mbpp_744_code import check_none

class TestCheckNone(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertTrue(check_none(()))

    def test_single_none_element(self):
        self.assertTrue(check_none((None, 1, 2)))

    def test_multiple_none_elements(self):
        self.assertTrue(check_none((None, None, 1)))

    def test_no_none_elements(self):
        self.assertFalse(check_none((1, 2, 3)))

    def test_mixed_types(self):
        self.assertFalse(check_none((1, 'str', None)))
