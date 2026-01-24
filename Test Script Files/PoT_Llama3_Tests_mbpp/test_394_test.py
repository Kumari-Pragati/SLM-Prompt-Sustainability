import unittest
from mbpp_394_code import check_distinct

class TestCheckDistinct(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_distinct((1, 2, 3)))

    def test_edge_case(self):
        self.assertFalse(check_distinct((1, 2, 2)))

    def test_edge_case2(self):
        self.assertFalse(check_distinct((1, 1, 1)))

    def test_edge_case3(self):
        self.assertTrue(check_distinct(()))

    def test_edge_case4(self):
        self.assertTrue(check_distinct((1)))

    def test_edge_case5(self):
        self.assertFalse(check_distinct((1, 1, 2)))

    def test_edge_case6(self):
        self.assertFalse(check_distinct((1, 2, 3, 1)))

    def test_edge_case7(self):
        self.assertFalse(check_distinct((1, 2, 3, 4, 1)))

    def test_edge_case8(self):
        self.assertFalse(check_distinct((1, 2, 3, 4, 5, 1)))

    def test_edge_case9(self):
        self.assertFalse(check_distinct((1, 2, 3, 4, 5, 6, 1)))

    def test_edge_case10(self):
        self.assertFalse(check_distinct((1, 2, 3, 4, 5, 6, 7, 1)))
