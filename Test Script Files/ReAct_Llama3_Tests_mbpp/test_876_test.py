import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_lcm_typical(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_lcm_edge1(self):
        self.assertEqual(lcm(1, 2), 2)

    def test_lcm_edge2(self):
        self.assertEqual(lcm(2, 1), 2)

    def test_lcm_edge3(self):
        self.assertEqual(lcm(3, 3), 3)

    def test_lcm_edge4(self):
        self.assertEqual(lcm(5, 5), 5)

    def test_lcm_edge5(self):
        self.assertEqual(lcm(10, 15), 30)

    def test_lcm_edge6(self):
        self.assertEqual(lcm(20, 25), 100)

    def test_lcm_edge7(self):
        self.assertEqual(lcm(30, 40), 120)

    def test_lcm_edge8(self):
        self.assertEqual(lcm(50, 75), 150)

    def test_lcm_edge9(self):
        self.assertEqual(lcm(100, 200), 200)

    def test_lcm_edge10(self):
        self.assertEqual(lcm(200, 300), 600)
