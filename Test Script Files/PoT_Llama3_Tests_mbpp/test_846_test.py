import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [3, 4, 5, 6, 7], 5), 3)

    def test_edge_case(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 2)

    def test_edge_case2(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], 6), 5)

    def test_edge_case3(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 5)

    def test_edge_case4(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5), 4)

    def test_edge_case5(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 5, 6], 5), 4)

    def test_edge_case6(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 7], 5), 4)

    def test_edge_case7(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 5, 6, 7], 6), 4)

    def test_edge_case8(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], 7), 5)

    def test_edge_case9(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8], 8), 5)

    def test_edge_case10(self):
        self.assertEqual(find_platform([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 5)
