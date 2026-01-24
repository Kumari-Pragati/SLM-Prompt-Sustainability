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
        self.assertEqual(highest_Power_of_2(1), 1)

    def test_edge_case4(self):
        self.assertEqual(highest_Power_of_2(0), 0)

    def test_edge_case5(self):
        self.assertEqual(highest_Power_of_2(2), 2)

    def test_edge_case6(self):
        self.assertEqual(highest_Power_of_2(3), 2)

    def test_edge_case7(self):
        self.assertEqual(highest_Power_of_2(4), 4)

    def test_edge_case8(self):
        self.assertEqual(highest_Power_of_2(5), 2)

    def test_edge_case9(self):
        self.assertEqual(highest_Power_of_2(6), 2)

    def test_edge_case10(self):
        self.assertEqual(highest_Power_of_2(7), 2)

    def test_edge_case11(self):
        self.assertEqual(highest_Power_of_2(8), 8)

    def test_edge_case12(self):
        self.assertEqual(highest_Power_of_2(9), 2)

    def test_edge_case13(self):
        self.assertEqual(highest_Power_of_2(10), 2)

    def test_edge_case14(self):
        self.assertEqual(highest_Power_of_2(11), 2)

    def test_edge_case15(self):
        self.assertEqual(highest_Power_of_2(12), 2)

    def test_edge_case16(self):
        self.assertEqual(highest_Power_of_2(13), 2)

    def test_edge_case17(self):
        self.assertEqual(highest_Power_of_2(14), 2)

    def test_edge_case18(self):
        self.assertEqual(highest_Power_of_2(15), 8)

    def test_edge_case19(self):
        self.assertEqual(highest_Power_of_2(16), 16)

    def test_edge_case20(self):
        self.assertEqual(highest_Power_of_2(32), 32)
