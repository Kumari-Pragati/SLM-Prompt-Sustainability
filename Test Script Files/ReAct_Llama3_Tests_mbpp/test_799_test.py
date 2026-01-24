import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_left_rotate_typical(self):
        self.assertEqual(left_Rotate(1, 2), 4)

    def test_left_rotate_edge(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge2(self):
        self.assertEqual(left_Rotate(1, 0), 1)

    def test_left_rotate_edge3(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge4(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge5(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge6(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge7(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge8(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge9(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge10(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge11(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge12(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge13(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge14(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge15(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge16(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge17(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge18(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge19(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge20(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge21(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge22(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge23(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge24(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge25(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge26(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge27(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge28(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge29(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge30(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge31(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge32(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge33(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge34(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge35(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge36(self):
        self.assertEqual(left_Rotate(1, 30), 2)

    def test_left_rotate_edge37(self):
        self.assertEqual(left_Rotate(1, 31), 1)

    def test_left_rotate_edge38(self):
        self.assertEqual(left_Rotate(1, 32), 1)

    def test_left_rotate_edge39(self):
        self.assertEqual(left_Rotate(1, 33), 1)

    def test_left_rotate_edge40(self):
        self.assertEqual(left_Rotate(1, 1), 2)

    def test_left_rotate_edge41(self):
        self.assertEqual(left_Rotate(1, 30