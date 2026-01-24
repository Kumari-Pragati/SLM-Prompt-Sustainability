import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):
    def test_valid_input(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_invalid_input(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_empty_input(self):
        self.assertTrue(check_valid(()))

    def test_single_element_input(self):
        self.assertTrue(check_valid((True,)))

    def test_all_falses_input(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_mixed_input(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_single_true_input(self):
        self.assertTrue(check_valid((True,)))

    def test_all_trues_input(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_valid("test")

    def test_invalid_input_structure(self):
        with self.assertRaises(TypeError):
            check_valid([1, 2, 3])
