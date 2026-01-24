import unittest
from mbpp_829_code import second_frequent

class TestSecondFrequent(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(second_frequent([1, 2, 2, 3, 3, 3]), 3)

    def test_edge_case(self):
        self.assertEqual(second_frequent([1, 1, 1, 2]), 2)

    def test_edge_case2(self):
        self.assertEqual(second_frequent([1, 2, 3, 4, 5]), 4)

    def test_edge_case3(self):
        self.assertEqual(second_frequent([1, 1, 1, 1, 1]), 1)

    def test_edge_case4(self):
        self.assertEqual(second_frequent([]), None)

    def test_edge_case5(self):
        self.assertEqual(second_frequent([1]), 1)

    def test_edge_case6(self):
        self.assertEqual(second_frequent([1, 2, 3, 4, 5, 6]), 5)

    def test_edge_case7(self):
        self.assertEqual(second_frequent([1, 1, 1, 1, 1, 1]), 1)

    def test_edge_case8(self):
        self.assertEqual(second_frequent([1, 2, 3, 4, 5, 6, 7]), 5)
