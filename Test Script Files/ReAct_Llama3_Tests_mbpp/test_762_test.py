import unittest
from mbpp_762_code import check_monthnumber_number

class TestCheckMonthnumberNumber(unittest.TestCase):

    def test_typical_case_true(self):
        self.assertTrue(check_monthnumber_number(4))

    def test_typical_case_true2(self):
        self.assertTrue(check_monthnumber_number(6))

    def test_typical_case_true3(self):
        self.assertTrue(check_monthnumber_number(9))

    def test_typical_case_true4(self):
        self.assertTrue(check_monthnumber_number(11))

    def test_typical_case_false(self):
        self.assertFalse(check_monthnumber_number(1))

    def test_typical_case_false2(self):
        self.assertFalse(check_monthnumber_number(2))

    def test_typical_case_false3(self):
        self.assertFalse(check_monthnumber_number(3))

    def test_typical_case_false4(self):
        self.assertFalse(check_monthnumber_number(5))

    def test_typical_case_false5(self):
        self.assertFalse(check_monthnumber_number(7))

    def test_typical_case_false6(self):
        self.assertFalse(check_monthnumber_number(8))

    def test_typical_case_false7(self):
        self.assertFalse(check_monthnumber_number(10))

    def test_typical_case_false8(self):
        self.assertFalse(check_monthnumber_number(12))

    def test_edge_case(self):
        self.assertFalse(check_monthnumber_number(13))

    def test_edge_case2(self):
        self.assertFalse(check_monthnumber_number(0))

    def test_edge_case3(self):
        self.assertFalse(check_monthnumber_number(15))

    def test_edge_case4(self):
        self.assertFalse(check_monthnumber_number(16))

    def test_edge_case5(self):
        self.assertFalse(check_monthnumber_number(17))

    def test_edge_case6(self):
        self.assertFalse(check_monthnumber_number(18))

    def test_edge_case7(self):
        self.assertFalse(check_monthnumber_number(19))

    def test_edge_case8(self):
        self.assertFalse(check_monthnumber_number(20))
