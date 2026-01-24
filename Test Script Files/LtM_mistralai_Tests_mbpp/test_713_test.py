import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_simple_true(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_simple_false(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_mixed(self):
        self.assertTrue(check_valid((True, False, True)))
        self.assertFalse(check_valid((False, True, False)))

    def test_single_element(self):
        self.assertTrue(check_valid((True,)))
        self.assertFalse(check_valid((False,)))

    def test_empty_list(self):
        self.assertRaises(TypeError, check_valid, ())
