import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_case2(self):
        self.assertEqual(max_volume(2), 0)

    def test_edge_case3(self):
        self.assertEqual(max_volume(4), 6)

    def test_edge_case4(self):
        self.assertEqual(max_volume(5), 24)

    def test_edge_case5(self):
        self.assertEqual(max_volume(6), 36)

    def test_edge_case6(self):
        self.assertEqual(max_volume(7), 60)

    def test_edge_case7(self):
        self.assertEqual(max_volume(8), 80)

    def test_edge_case8(self):
        self.assertEqual(max_volume(9), 108)

    def test_edge_case9(self):
        self.assertEqual(max_volume(10), 120)

    def test_edge_case10(self):
        self.assertEqual(max_volume(11), 132)

    def test_edge_case11(self):
        self.assertEqual(max_volume(12), 144)

    def test_edge_case12(self):
        self.assertEqual(max_volume(13), 156)

    def test_edge_case13(self):
        self.assertEqual(max_volume(14), 168)

    def test_edge_case14(self):
        self.assertEqual(max_volume(15), 180)

    def test_edge_case15(self):
        self.assertEqual(max_volume(16), 192)

    def test_edge_case16(self):
        self.assertEqual(max_volume(17), 204)

    def test_edge_case17(self):
        self.assertEqual(max_volume(18), 216)

    def test_edge_case18(self):
        self.assertEqual(max_volume(19), 228)

    def test_edge_case19(self):
        self.assertEqual(max_volume(20), 240)

    def test_edge_case20(self):
        self.assertEqual(max_volume(21), 252)

    def test_edge_case21(self):
        self.assertEqual(max_volume(22), 264)

    def test_edge_case22(self):
        self.assertEqual(max_volume(23), 276)

    def test_edge_case23(self):
        self.assertEqual(max_volume(24), 288)

    def test_edge_case24(self):
        self.assertEqual(max_volume(25), 300)

    def test_edge_case25(self):
        self.assertEqual(max_volume(26), 312)

    def test_edge_case26(self):
        self.assertEqual(max_volume(27), 324)

    def test_edge_case27(self):
        self.assertEqual(max_volume(28), 336)

    def test_edge_case28(self):
        self.assertEqual(max_volume(29), 348)

    def test_edge_case29(self):
        self.assertEqual(max_volume(30), 360)
