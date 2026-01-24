import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertFalse(check_valid(()))

    def test_single_false_tuple(self):
        self.assertTrue(check_valid((False,)))

    def test_multiple_false_tuples(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_single_true_tuple(self):
        self.assertTrue(check_valid((True,)))

    def test_multiple_true_tuples(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_mixed_tuples(self):
        self.assertFalse(check_valid((True, False, True)))
