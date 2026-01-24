import unittest
from mbpp_903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Unset_Bits(0), 0)
        self.assertEqual(count_Unset_Bits(1), 0)
        self.assertEqual(count_Unset_Bits(2), 1)
        self.assertEqual(count_Unset_Bits(3), 1)
        self.assertEqual(count_Unset_Bits(4), 2)
        self.assertEqual(count_Unset_Bits(5), 2)

    def test_edge(self):
        self.assertEqual(count_Unset_Bits(8), 1)
        self.assertEqual(count_Unset_Bits(16), 4)
        self.assertEqual(count_Unset_Bits(32), 5)
        self.assertEqual(count_Unset_Bits(64), 6)
        self.assertEqual(count_Unset_Bits(128), 7)

    def test_max(self):
        self.assertEqual(count_Unset_Bits(255), 8)
        self.assertEqual(count_Unset_Bits(256), 8)
        self.assertEqual(count_Unset_Bits(512), 9)
        self.assertEqual(count_Unset_Bits(1024), 10)

    def test_max_edge(self):
        self.assertEqual(count_Unset_Bits(2047), 11)
        self.assertEqual(count_Unset_Bits(2048), 11)
        self.assertEqual(count_Unset_Bits(4095), 12)
        self.assertEqual(count_Unset_Bits(4096), 12)

    def test_max_edge2(self):
        self.assertEqual(count_Unset_Bits(8191), 13)
        self.assertEqual(count_Unset_Bits(8192), 13)
        self.assertEqual(count_Unset_Bits(16383), 14)
        self.assertEqual(count_Unset_Bits(16384), 14)

    def test_max_edge3(self):
        self.assertEqual(count_Unset_Bits(32767), 15)
        self.assertEqual(count_Unset_Bits(32768), 15)
        self.assertEqual(count_Unset_Bits(65535), 16)
        self.assertEqual(count_Unset_Bits(65536), 16)

    def test_max_edge4(self):
        self.assertEqual(count_Unset_Bits(131071), 17)
        self.assertEqual(count_Unset_Bits(131072), 17)
        self.assertEqual(count_Unset_Bits(262143), 18)
        self.assertEqual(count_Unset_Bits(262144), 18)

    def test_max_edge5(self):
        self.assertEqual(count_Unset_Bits(524287), 19)
        self.assertEqual(count_Unset_Bits(524288), 19)
        self.assertEqual(count_Unset_Bits(1048575), 20)
        self.assertEqual(count_Unset_Bits(1048576), 20)

    def test_max_edge6(self):
        self.assertEqual(count_Unset_Bits(2097151), 21)
        self.assertEqual(count_Unset_Bits(2097152), 21)
        self.assertEqual(count_Unset_Bits(4194303), 22)
        self.assertEqual(count_Unset_Bits(4194304), 22)

    def test_max_edge7(self):
        self.assertEqual(count_Unset_Bits(8388607), 23)
        self.assertEqual(count_Unset_Bits(8388608), 23)
        self.assertEqual(count_Unset_Bits(16777215), 24)
        self.assertEqual(count_Unset_Bits(16777216), 24)

    def test_max_edge8(self):
        self.assertEqual(count_Unset_Bits(33554431), 25)
        self.assertEqual(count_Unset_Bits(33554432), 25)
        self.assertEqual(count_Unset_Bits(67108863), 26)
        self.assertEqual(count_Unset_Bits(67108864), 26)

    def test_max_edge9(self):
        self.assertEqual(count_Unset_Bits(134217727), 27)
        self.assertEqual(count_Unset_Bits(134217728), 27)
        self.assertEqual(count_Unset_Bits(268435455), 28)
        self.assertEqual(count_Unset_Bits(268435456), 28)

    def test_max_edge10(self):
        self.assertEqual(count_Unset_Bits(536870911), 29)
        self.assertEqual(count_Unset_Bits(536870912), 29)
        self.assertEqual(count_Unset_Bits(1073741823), 30)
        self.assertEqual(count_Unset_Bits(1073741824), 30)
