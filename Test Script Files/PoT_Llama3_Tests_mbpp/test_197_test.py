import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), (8, 32))

    def test_edge_case(self):
        self.assertEqual(find_exponentio((0, 0), (0, 0)), (1, 1))

    def test_edge_case2(self):
        self.assertEqual(find_exponentio((1, 1), (1, 1)), (1, 1))

    def test_edge_case3(self):
        self.assertEqual(find_exponentio((1, 2), (2, 1)), (1, 4))

    def test_edge_case4(self):
        self.assertEqual(find_exponentio((2, 3), (3, 2)), (8, 9))

    def test_edge_case5(self):
        self.assertEqual(find_exponentio((1, 1), (1, 1)), (1, 1))

    def test_edge_case6(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), (8, 32))

    def test_edge_case7(self):
        self.assertEqual(find_exponentio((1, 2), (2, 1)), (1, 4))

    def test_edge_case8(self):
        self.assertEqual(find_exponentio((2, 3), (3, 2)), (8, 9))

    def test_edge_case9(self):
        self.assertEqual(find_exponentio((1, 1), (1, 1)), (1, 1))

    def test_edge_case10(self):
        self.assertEqual(find_exponentio((2, 3), (4, 5)), (8, 32))
