import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case_s_1(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_case_s_2(self):
        self.assertEqual(max_volume(2), 0)

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
