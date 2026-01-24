import unittest
from mbpp_222_code import check_type

class TestCheckType(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(check_type((1, 2, 3)))

    def test_edge_case(self):
        self.assertFalse(check_type((1, '2', 3)))

    def test_edge_case2(self):
        self.assertFalse(check_type((1, 2, '3')))

    def test_edge_case3(self):
        self.assertFalse(check_type((1, 2, 3.0)))

    def test_edge_case4(self):
        self.assertFalse(check_type((1, 2, 3, 4)))

    def test_edge_case5(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5)))

    def test_edge_case6(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6)))

    def test_edge_case7(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7)))

    def test_edge_case8(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8)))

    def test_edge_case9(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9)))

    def test_edge_case10(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

    def test_edge_case11(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

    def test_edge_case12(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

    def test_edge_case13(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

    def test_edge_case14(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))

    def test_edge_case15(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

    def test_edge_case16(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))

    def test_edge_case17(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))

    def test_edge_case18(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))

    def test_edge_case19(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))

    def test_edge_case20(self):
        self.assertFalse(check_type((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
