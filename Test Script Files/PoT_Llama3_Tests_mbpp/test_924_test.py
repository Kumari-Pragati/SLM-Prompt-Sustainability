import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_of_two(5, 3), 5)

    def test_typical_case2(self):
        self.assertEqual(max_of_two(3, 5), 5)

    def test_edge_case(self):
        self.assertEqual(max_of_two(5, 5), 5)

    def test_edge_case2(self):
        self.assertEqual(max_of_two(-5, -5), -5)

    def test_edge_case3(self):
        self.assertEqual(max_of_two(0, 0), 0)

    def test_edge_case4(self):
        self.assertEqual(max_of_two(-5, 0), 0)

    def test_edge_case5(self):
        self.assertEqual(max_of_two(0, -5), 0)

    def test_edge_case6(self):
        self.assertEqual(max_of_two(-5, 5), 5)

    def test_edge_case7(self):
        self.assertEqual(max_of_two(5, -5), 5)

    def test_edge_case8(self):
        self.assertEqual(max_of_two(-5, 3), 3)

    def test_edge_case9(self):
        self.assertEqual(max_of_two(3, -5), 3)

    def test_edge_case10(self):
        self.assertEqual(max_of_two(-5, -3), -3)

    def test_edge_case11(self):
        self.assertEqual(max_of_two(3, 5), 5)

    def test_edge_case12(self):
        self.assertEqual(max_of_two(5, 3), 5)
