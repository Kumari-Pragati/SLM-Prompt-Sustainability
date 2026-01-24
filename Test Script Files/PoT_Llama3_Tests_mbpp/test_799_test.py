import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_Rotate(5, 2), 10)

    def test_edge_case(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_edge_case2(self):
        self.assertEqual(left_Rotate(0, 0), 0)

    def test_edge_case3(self):
        self.assertEqual(left_Rotate(1, 0), 1)

    def test_edge_case4(self):
        self.assertEqual(left_Rotate(2**31 - 1, 1), 2**31 - 2**30)

    def test_edge_case5(self):
        self.assertEqual(left_Rotate(-1, 1), -2)

    def test_edge_case6(self):
        self.assertEqual(left_Rotate(-2**31, 1), -2**31 + 2**30)

    def test_edge_case7(self):
        self.assertEqual(left_Rotate(2**31 - 1, 32), 2**31 - 2**30)

    def test_edge_case8(self):
        self.assertEqual(left_Rotate(-2**31, 32), -2**31 + 2**30)

    def test_edge_case9(self):
        self.assertEqual(left_Rotate(2**31 - 1, 33), 2**31 - 2**30)

    def test_edge_case10(self):
        self.assertEqual(left_Rotate(-2**31, 33), -2**31 + 2**30)
