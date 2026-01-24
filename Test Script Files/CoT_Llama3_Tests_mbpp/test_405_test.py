import unittest
from mbpp_405_code import check_tuplex

class TestCheckTuplex(unittest.TestCase):

    def test_true(self):
        self.assertTrue(check_tuplex([1,2,3,4], [1,2,3,4]))

    def test_false(self):
        self.assertFalse(check_tuplex([1,2,3,4], [5,6,7,8]))

    def test_edge_case1(self):
        self.assertTrue(check_tuplex([1,2,3,4], [1,2,3]))

    def test_edge_case2(self):
        self.assertFalse(check_tuplex([1,2,3,4], [5,6,7]))

    def test_edge_case3(self):
        self.assertTrue(check_tuplex([1,2,3,4], [4]))

    def test_edge_case4(self):
        self.assertFalse(check_tuplex([1,2,3,4], [5]))

    def test_edge_case5(self):
        self.assertTrue(check_tuplex([1,2,3,4], [1]))

    def test_edge_case6(self):
        self.assertFalse(check_tuplex([1,2,3,4], [5]))

    def test_edge_case7(self):
        self.assertTrue(check_tuplex([1,2,3,4], [1,2,3,4,5]))

    def test_edge_case8(self):
        self.assertFalse(check_tuplex([1,2,3,4], [5,6,7,8,9]))
