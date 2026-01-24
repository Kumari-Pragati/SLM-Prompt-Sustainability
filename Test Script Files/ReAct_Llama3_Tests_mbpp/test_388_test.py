import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(highest_Power_of_2(16), 16)

    def test_edge_case(self):
        self.assertEqual(highest_Power_of_2(15), 8)

    def test_edge_case2(self):
        self.assertEqual(highest_Power_of_2(32), 32)

    def test_edge_case3(self):
        self.assertEqual(highest_Power_of_2(64), 64)

    def test_edge_case4(self):
        self.assertEqual(highest_Power_of_2(128), 128)

    def test_edge_case5(self):
        self.assertEqual(highest_Power_of_2(256), 256)

    def test_edge_case6(self):
        self.assertEqual(highest_Power_of_2(512), 512)

    def test_edge_case7(self):
        self.assertEqual(highest_Power_of_2(1024), 1024)

    def test_edge_case8(self):
        self.assertEqual(highest_Power_of_2(2048), 2048)

    def test_edge_case9(self):
        self.assertEqual(highest_Power_of_2(4096), 4096)

    def test_edge_case10(self):
        self.assertEqual(highest_Power_of_2(8192), 8192)

    def test_edge_case11(self):
        self.assertEqual(highest_Power_of_2(16384), 16384)

    def test_edge_case12(self):
        self.assertEqual(highest_Power_of_2(32768), 32768)

    def test_edge_case13(self):
        self.assertEqual(highest_Power_of_2(65536), 65536)

    def test_edge_case14(self):
        self.assertEqual(highest_Power_of_2(131072), 131072)

    def test_edge_case15(self):
        self.assertEqual(highest_Power_of_2(262144), 262144)

    def test_edge_case16(self):
        self.assertEqual(highest_Power_of_2(524288), 524288)

    def test_edge_case17(self):
        self.assertEqual(highest_Power_of_2(1048576), 1048576)

    def test_edge_case18(self):
        self.assertEqual(highest_Power_of_2(2097152), 2097152)

    def test_edge_case19(self):
        self.assertEqual(highest_Power_of_2(4194304), 4194304)

    def test_edge_case20(self):
        self.assertEqual(highest_Power_of_2(8388608), 8388608)

    def test_edge_case21(self):
        self.assertEqual(highest_Power_of_2(16777216), 16777216)

    def test_edge_case22(self):
        self.assertEqual(highest_Power_of_2(33554432), 33554432)

    def test_edge_case23(self):
        self.assertEqual(highest_Power_of_2(67108864), 67108864)

    def test_edge_case24(self):
        self.assertEqual(highest_Power_of_2(134217728), 134217728)

    def test_edge_case25(self):
        self.assertEqual(highest_Power_of_2(268435456), 268435456)

    def test_edge_case26(self):
        self.assertEqual(highest_Power_of_2(536870912), 536870912)

    def test_edge_case27(self):
        self.assertEqual(highest_Power_of_2(1073741824), 1073741824)

    def test_edge_case28(self):
        self.assertEqual(highest_Power_of_2(2147483648), 2147483648)

    def test_edge_case29(self):
        self.assertEqual(highest_Power_of_2(4294967296), 4294967296)

    def test_edge_case30(self):
        self.assertEqual(highest_Power_of_2(8589934592), 8589934592)

    def test_edge_case31(self):
        self.assertEqual(highest_Power_of_2(17179869184), 17179869184)

    def test_edge_case32(self):
        self.assertEqual(highest_Power_of_2(34359738368), 34359738368)

    def test_edge_case33(self):
        self.assertEqual(highest_Power_of_2(68719476736), 68719476736)

    def test_edge_case34(self):
        self.assertEqual(highest_Power_of_2(137438953472), 137438953472)

    def test_edge_case35(self):
        self.assertEqual(highest_Power_of_2(274877906944), 274877906944)

    def test_edge_case36(self):
        self.assertEqual(highest_Power_of_2(549945