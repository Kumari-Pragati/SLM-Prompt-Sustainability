import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(min_difference([(1, 3), (2, 4)]), 1)

    def test_edge(self):
        self.assertEqual(min_difference([(1, 1), (2, 2)]), 0)

    def test_edge2(self):
        self.assertEqual(min_difference([(1, 2), (2, 1)]), 1)

    def test_edge3(self):
        self.assertEqual(min_difference([(1, 3), (2, 2)]), 1)

    def test_edge4(self):
        self.assertEqual(min_difference([(1, 1), (2, 3)]), 1)

    def test_edge5(self):
        self.assertEqual(min_difference([(1, 2), (2, 3)]), 1)

    def test_edge6(self):
        self.assertEqual(min_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_edge7(self):
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4)]), 1)

    def test_edge8(self):
        self.assertEqual(min_difference([(1, 1), (2, 2), (3, 4)]), 1)

    def test_edge9(self):
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 1)]), 1)

    def test_edge10(self):
        self.assertEqual(min_difference([(1, 2), (2, 3), (3, 4), (4, 5)]), 1)
