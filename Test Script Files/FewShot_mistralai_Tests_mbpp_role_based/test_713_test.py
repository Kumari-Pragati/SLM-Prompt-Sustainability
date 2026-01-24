import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_mixed_input(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_all_false(self):
        self.assertTrue(check_valid((False, False, False)))

    def test_empty_tuple(self):
        self.AssertRaises(TypeError, check_valid, ())

    def test_single_element_tuple(self):
        self.AssertRaises(TypeError, check_valid, (True,))
