import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rearrange_bigger(12345), 54321)

    def test_edge_case_1(self):
        self.assertEqual(rearrange_bigger(11111), 11111)

    def test_edge_case_2(self):
        self.assertEqual(rearrange_bigger(22222), 22222)

    def test_edge_case_3(self):
        self.assertEqual(rearrange_bigger(33333), 33333)

    def test_edge_case_4(self):
        self.assertEqual(rearrange_bigger(44444), 44444)

    def test_edge_case_5(self):
        self.assertEqual(rearrange_bigger(55555), 55555)

    def test_edge_case_6(self):
        self.assertEqual(rearrange_bigger(66666), 66666)

    def test_edge_case_7(self):
        self.assertEqual(rearrange_bigger(77777), 77777)

    def test_edge_case_8(self):
        self.assertEqual(rearrange_bigger(88888), 88888)

    def test_edge_case_9(self):
        self.assertEqual(rearrange_bigger(99999), 99999)

    def test_edge_case_10(self):
        self.assertEqual(rearrange_bigger(101010), 101010)

    def test_edge_case_11(self):
        self.assertEqual(rearrange_bigger(111111), 111111)

    def test_edge_case_12(self):
        self.assertEqual(rearrange_bigger(123456), 654321)

    def test_edge_case_13(self):
        self.assertEqual(rearrange_bigger(1234567), 7654321)

    def test_edge_case_14(self):
        self.assertEqual(rearrange_bigger(12345678), 87654321)

    def test_edge_case_15(self):
        self.assertEqual(rearrange_bigger(123456789), 987654321)

    def test_edge_case_16(self):
        self.assertEqual(rearrange_bigger(1234567890), 0987654321)

    def test_edge_case_17(self):
        self.assertEqual(rearrange_bigger(12345678901), 0123456789)

    def test_edge_case_18(self):
        self.assertEqual(rearrange_bigger(123456789012), 1234567890)

    def test_edge_case_19(self):
        self.assertEqual(rearrange_bigger(1234567890123), 3456789012)

    def test_edge_case_20(self):
        self.assertEqual(rearrange_bigger(12345678901234), 4567890123)

    def test_edge_case_21(self):
        self.assertEqual(rearrange_bigger(123456789012345), 5678901234)

    def test_edge_case_22(self):
        self.assertEqual(rearrange_bigger(1234567890123456), 6789012345)

    def test_edge_case_23(self):
        self.assertEqual(rearrange_bigger(12345678901234567), 7890123456)

    def test_edge_case_24(self):
        self.assertEqual(rearrange_bigger(123456789012345678), 8901234567)

    def test_edge_case_25(self):
        self.assertEqual(rearrange_bigger(1234567890123456789), 9012345678)

    def test_edge_case_26(self):
        self.assertEqual(rearrange_bigger(123456789012345678901), 0123456789)

    def test_edge_case_27(self):
        self.assertEqual(rearrange_bigger(1234567890123456789012), 1234567890)

    def test_edge_case_28(self):
        self.assertEqual(rearrange_bigger(12345678901234567890123), 3456789012)

    def test_edge_case_29(self):
        self.assertEqual(rearrange_bigger(123456789012345678901234), 4567890123)

    def test_edge_case_30(self):
        self.assertEqual(rearrange_bigger(1234567890123456789012345), 5678901234)

    def test_edge_case_31(self):
        self.assertEqual(rearrange_bigger(12345678901234567890123456), 6789012345)

    def test_edge_case_32(self):
        self.assertEqual(rearrange_bigger(123456789012345678901234567), 7890123456)

    def test_edge_case_33(self):
        self.assertEqual(rearrange_bigger(1234567890123456789012345678), 8901234567)

    def test_edge_case_34(self):
        self.assertEqual(rearrange_bigger(123456789012345678