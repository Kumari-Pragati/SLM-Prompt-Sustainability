import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case_s_1(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_case_s_2(self):
        self.assertEqual(max_volume(2), 1)

    def test_edge_case_s_3(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case_s_4(self):
        self.assertEqual(max_volume(4), 24)

    def test_edge_case_s_5(self):
        self.assertEqual(max_volume(5), 60)

    def test_edge_case_s_6(self):
        self.assertEqual(max_volume(6), 120)

    def test_edge_case_s_7(self):
        self.assertEqual(max_volume(7), 210)

    def test_edge_case_s_8(self):
        self.assertEqual(max_volume(8), 336)

    def test_edge_case_s_9(self):
        self.assertEqual(max_volume(9), 504)

    def test_edge_case_s_10(self):
        self.assertEqual(max_volume(10), 720)

    def test_edge_case_s_11(self):
        self.assertEqual(max_volume(11), 990)

    def test_edge_case_s_12(self):
        self.assertEqual(max_volume(12), 1320)

    def test_edge_case_s_13(self):
        self.assertEqual(max_volume(13), 1716)

    def test_edge_case_s_14(self):
        self.assertEqual(max_volume(14), 2184)

    def test_edge_case_s_15(self):
        self.assertEqual(max_volume(15), 2730)

    def test_edge_case_s_16(self):
        self.assertEqual(max_volume(16), 3376)

    def test_edge_case_s_17(self):
        self.assertEqual(max_volume(17), 4096)

    def test_edge_case_s_18(self):
        self.assertEqual(max_volume(18), 4896)

    def test_edge_case_s_19(self):
        self.assertEqual(max_volume(19), 5824)

    def test_edge_case_s_20(self):
        self.assertEqual(max_volume(20), 6840)
