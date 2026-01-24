import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)

    def test_edge_case(self):
        self.assertEqual(count_Rotation([5, 4, 3, 2, 1], 5), 1)

    def test_edge_case2(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 1), 0)

    def test_edge_case3(self):
        self.assertEqual(count_Rotation([5, 5, 5, 5, 5], 5), 0)

    def test_edge_case4(self):
        self.assertEqual(count_Rotation([1, 1, 1, 1, 1], 5), 0)

    def test_edge_case5(self):
        self.assertEqual(count_Rotation([5, 1, 2, 3, 4], 5), 1)

    def test_edge_case6(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 0), None)

    def test_edge_case7(self):
        self.assertEqual(count_Rotation([], 5), None)

    def test_edge_case8(self):
        self.assertEqual(count_Rotation([1], 1), 0)

    def test_edge_case9(self):
        self.assertEqual(count_Rotation([1, 2], 2), 0)

    def test_edge_case10(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5, 6], 6), 0)
