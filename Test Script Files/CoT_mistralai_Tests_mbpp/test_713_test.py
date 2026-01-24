import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):
    def test_true_positive(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_false_positive(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_true_negative(self):
        self.assertTrue(check_valid((False, False, False)))

    def test_false_negative(self):
        self.assertFalse(check_valid((False, True, False)))

    def test_mixed_positive(self):
        self.assertTrue(check_valid((True, False, True, True)))

    def test_mixed_negative(self):
        self.assertFalse(check_valid((True, False, True, False)))

    def test_empty_tuple(self):
        self.assertRaises(TypeError, check_valid, ())

    def test_single_element_tuple(self):
        self.assertRaises(TypeError, check_valid, (True,))

    def test_multi_element_list(self):
        self.assertRaises(TypeError, check_valid, [1, 2, 3])
