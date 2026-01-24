import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):
    def test_equilateral(self):
        self.assertTrue(check_equilateral(1,1,1))
    def test_non_equilateral(self):
        self.assertFalse(check_equilateral(1,2,3))
    def test_edge_case(self):
        self.assertTrue(check_equilateral(1,1,1))
    def test_edge_case2(self):
        self.assertFalse(check_equilateral(1,1,2))
