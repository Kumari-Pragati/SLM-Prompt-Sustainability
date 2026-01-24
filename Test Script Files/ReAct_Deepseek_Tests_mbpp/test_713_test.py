import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_typical_case_all_true(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_typical_case_all_false(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_typical_case_mixed(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_edge_case_empty_tuple(self):
        self.assertTrue(check_valid(()))

    def test_edge_case_single_true(self):
        self.assertTrue(check_valid((True,)))

    def test_edge_case_single_false(self):
        self.assertFalse(check_valid((False,)))

    def test_error_case_non_boolean_elements(self):
        with self.assertRaises(TypeError):
            check_valid((1, 2, 3))

    def test_error_case_non_iterable(self):
        with self.assertRaises(TypeError):
            check_valid(1)
