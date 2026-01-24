import unittest
from mbpp_801_code import test_three_equal

class TestTestThreeEqual(unittest.TestCase):
    def test_three_equal_typical(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_edge1(self):
        self.assertEqual(test_three_equal(1, 1, 1), 2)

    def test_three_equal_edge2(self):
        self.assertEqual(test_three_equal(1, 2, 2), 1)

    def test_three_equal_edge3(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_edge4(self):
        self.assertEqual(test_three_equal(1, 1, 2), 1)

    def test_three_equal_edge5(self):
        self.assertEqual(test_three_equal(1, 1, 1), 2)

    def test_three_equal_edge6(self):
        self.assertEqual(test_three_equal(1, 2, 1), 1)

    def test_three_equal_edge7(self):
        self.assertEqual(test_three_equal(1, 1, 1), 2)

    def test_three_equal_edge8(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_edge9(self):
        self.assertEqual(test_three_equal(1, 1, 2), 1)

    def test_three_equal_edge10(self):
        self.assertEqual(test_three_equal(1, 1, 1), 2)
