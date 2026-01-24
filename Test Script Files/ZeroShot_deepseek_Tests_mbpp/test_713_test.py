import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_all_true(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_all_false(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_mixed(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_empty(self):
        self.assertTrue(check_valid(()))

    def test_single_true(self):
        self.assertTrue(check_valid((True,)))

    def test_single_false(self):
        self.assertFalse(check_valid((False,)))
