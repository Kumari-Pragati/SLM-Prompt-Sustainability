import unittest
from mbpp_713_code import check_valid

class TestCheckValid(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_valid((True, True, True)))

    def test_single_false(self):
        self.assertFalse(check_valid((True, False, True)))

    def test_all_false(self):
        self.assertFalse(check_valid((False, False, False)))

    def test_empty_tuple(self):
        self.assertTrue(check_valid(()))

    def test_single_true(self):
        self.assertTrue(check_valid((True,)))

    def test_mixed_types(self):
        self.assertFalse(check_valid((True, 'test', 123)))

    def test_none_in_tuple(self):
        with self.assertRaises(TypeError):
            check_valid((None,))
