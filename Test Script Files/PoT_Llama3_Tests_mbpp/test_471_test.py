import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 2)

    def test_edge_case(self):
        self.assertEqual(find_remainder([1, 2, 3], 1, 5), 1)

    def test_edge_case2(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 1), 1)

    def test_edge_case3(self):
        self.assertEqual(find_remainder([1, 2, 3], 0, 5), 1)

    def test_edge_case4(self):
        self.assertEqual(find_remainder([], 0, 5), 1)

    def test_edge_case5(self):
        self.assertEqual(find_remainder([1], 1, 5), 1)

    def test_edge_case6(self):
        self.assertEqual(find_remainder([1, 2, 3], 4, 5), 2)

    def test_edge_case7(self):
        self.assertEqual(find_remainder([1, 2, 3], 5, 5), 1)

    def test_edge_case8(self):
        self.assertEqual(find_remainder([1, 2, 3], 6, 5), 2)

    def test_edge_case9(self):
        self.assertEqual(find_remainder([1, 2, 3], 7, 5), 2)

    def test_edge_case10(self):
        self.assertEqual(find_remainder([1, 2, 3], 8, 5), 2)
