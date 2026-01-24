import unittest
from mbpp_407_code import rearrange_bigger

class TestRearrangeBigger(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rearrange_bigger(12345), 54321)

    def test_edge_case(self):
        self.assertEqual(rearrange_bigger(123), 321)

    def test_edge_case2(self):
        self.assertEqual(rearrange_bigger(111), 111)

    def test_edge_case3(self):
        self.assertEqual(rearrange_bigger(123456), 654321)

    def test_edge_case4(self):
        self.assertEqual(rearrange_bigger(123456789), 987654321)

    def test_edge_case5(self):
        self.assertEqual(rearrange_bigger(1234567890), 9876543210)

    def test_edge_case6(self):
        self.assertEqual(rearrange_bigger(111111111), 111111111)

    def test_edge_case7(self):
        self.assertEqual(rearrange_bigger(1111111111), 1111111111)

    def test_edge_case8(self):
        self.assertEqual(rearrange_bigger(11111111111), 11111111111)

    def test_edge_case9(self):
        self.assertEqual(rearrange_bigger(123456789012), 987654321012)

    def test_edge_case10(self):
        self.assertEqual(rearrange_bigger(1234567890123), 9876543210123)

    def test_edge_case11(self):
        self.assertEqual(rearrange_bigger(12345678901234), 98765432101234)

    def test_edge_case12(self):
        self.assertEqual(rearrange_bigger(123456789012345), 987654321012345)

    def test_edge_case13(self):
        self.assertEqual(rearrange_bigger(1234567890123456), 9876543210123456)

    def test_edge_case14(self):
        self.assertEqual(rearrange_bigger(12345678901234567), 98765432101234567)

    def test_edge_case15(self):
        self.assertEqual(rearrange_bigger(123456789012345678), 987654321012345678)

    def test_edge_case16(self):
        self.assertEqual(rearrange_bigger(1234567890123456789), 9876543210123456789)

    def test_edge_case17(self):
        self.assertEqual(rearrange_bigger(12345678901234567890), 98765432101234567890)

    def test_edge_case18(self):
        self.assertEqual(rearrange_bigger(123456789012345678901), 987654321012345678901)

    def test_edge_case19(self):
        self.assertEqual(rearrange_bigger(123456789012345678902), 987654321012345678902)

    def test_edge_case20(self):
        self.assertEqual(rearrange_bigger(123456789012345678903), 987654321012345678903)

    def test_edge_case21(self):
        self.assertEqual(rearrange_bigger(123456789012345678904), 987654321012345678904)

    def test_edge_case22(self):
        self.assertEqual(rearrange_bigger(123456789012345678905), 987654321012345678905)

    def test_edge_case23(self):
        self.assertEqual(rearrange_bigger(123456789012345678906), 987654321012345678906)

    def test_edge_case24(self):
        self.assertEqual(rearrange_bigger(123456789012345678907), 987654321012345678907)

    def test_edge_case25(self):
        self.assertEqual(rearrange_bigger(123456789012345678908), 987654321012345678908)

    def test_edge_case26(self):
        self.assertEqual(rearrange_bigger(123456789012345678909), 987654321012345678909)

    def test_edge_case27(self):
        self.assertEqual(rearrange_bigger(123456789012345678910), 987654321012345678910)

    def test_edge_case28(self):
        self.assertEqual(rearrange_bigger(123456789012345678911), 987654321012345678911)

    def test_edge_case29(self):
        self.assertEqual(rearrange_bigger(123456789012345678912), 987654321012345678912)

    def test_edge_case30(self):
        self.assertEqual(rearrange_bigger(123456789012345678913), 987654321012345678913)

    def test_edge_case31(self):
        self.assertEqual(rearrange_bigger(123456789012345678914), 987654321012345678914)

    def test_edge_case32(self):
        self.assertEqual(rearrange_bigger