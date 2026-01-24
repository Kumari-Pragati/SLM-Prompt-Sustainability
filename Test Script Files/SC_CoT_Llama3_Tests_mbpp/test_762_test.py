import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthnumberNumber(unittest.TestCase):

    def test_typical_true(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertTrue(check_monthnumber_number(6))
        self.assertTrue(check_monthnumber_number(9))
        self.assertTrue(check_monthnumber_number(11))

    def test_typical_false(self):
        self.assertFalse(check_monthnumber_number(1))
        self.assertFalse(check_monthnumber_number(2))
        self.assertFalse(check_monthnumber_number(3))
        self.assertFalse(check_monthnumber_number(5))
        self.assertFalse(check_monthnumber_number(7))
        self.assertFalse(check_monthnumber_number(8))
        self.assertFalse(check_monthnumber_number(10))
        self.assertFalse(check_monthnumber_number(12))
        self.assertFalse(check_monthnumber_number(13))

    def test_edge_case(self):
        self.assertTrue(check_monthnumber_number(4))
        self.assertFalse(check_monthnumber_number(13))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_monthnumber_number('a')
