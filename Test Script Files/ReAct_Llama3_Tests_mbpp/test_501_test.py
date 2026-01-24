import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_comm_div(12, 15), 2)

    def test_edge_case1(self):
        self.assertEqual(num_comm_div(1, 1), 2)

    def test_edge_case2(self):
        self.assertEqual(num_comm_div(2, 3), 2)

    def test_edge_case3(self):
        self.assertEqual(num_comm_div(4, 6), 2)

    def test_edge_case4(self):
        self.assertEqual(num_comm_div(8, 9), 2)

    def test_edge_case5(self):
        self.assertEqual(num_comm_div(10, 15), 2)

    def test_edge_case6(self):
        self.assertEqual(num_comm_div(12, 12), 1)

    def test_edge_case7(self):
        self.assertEqual(num_comm_div(15, 20), 2)

    def test_edge_case8(self):
        self.assertEqual(num_comm_div(24, 30), 2)

    def test_edge_case9(self):
        self.assertEqual(num_comm_div(36, 48), 2)

    def test_edge_case10(self):
        self.assertEqual(num_comm_div(50, 75), 2)

    def test_edge_case11(self):
        self.assertEqual(num_comm_div(60, 72), 2)

    def test_edge_case12(self):
        self.assertEqual(num_comm_div(80, 100), 2)

    def test_edge_case13(self):
        self.assertEqual(num_comm_div(100, 120), 2)

    def test_edge_case14(self):
        self.assertEqual(num_comm_div(120, 150), 2)

    def test_edge_case15(self):
        self.assertEqual(num_comm_div(150, 180), 2)

    def test_edge_case16(self):
        self.assertEqual(num_comm_div(180, 200), 2)

    def test_edge_case17(self):
        self.assertEqual(num_comm_div(200, 250), 2)

    def test_edge_case18(self):
        self.assertEqual(num_comm_div(250, 300), 2)

    def test_edge_case19(self):
        self.assertEqual(num_comm_div(300, 350), 2)

    def test_edge_case20(self):
        self.assertEqual(num_comm_div(350, 400), 2)

    def test_edge_case21(self):
        self.assertEqual(num_comm_div(400, 450), 2)

    def test_edge_case22(self):
        self.assertEqual(num_comm_div(450, 500), 2)

    def test_edge_case23(self):
        self.assertEqual(num_comm_div(500, 550), 2)

    def test_edge_case24(self):
        self.assertEqual(num_comm_div(550, 600), 2)

    def test_edge_case25(self):
        self.assertEqual(num_comm_div(600, 650), 2)

    def test_edge_case26(self):
        self.assertEqual(num_comm_div(650, 700), 2)

    def test_edge_case27(self):
        self.assertEqual(num_comm_div(700, 750), 2)

    def test_edge_case28(self):
        self.assertEqual(num_comm_div(750, 800), 2)

    def test_edge_case29(self):
        self.assertEqual(num_comm_div(800, 850), 2)

    def test_edge_case30(self):
        self.assertEqual(num_comm_div(850, 900), 2)

    def test_edge_case31(self):
        self.assertEqual(num_comm_div(900, 950), 2)

    def test_edge_case32(self):
        self.assertEqual(num_comm_div(950, 1000), 2)

    def test_edge_case33(self):
        self.assertEqual(num_comm_div(1000, 1050), 2)

    def test_edge_case34(self):
        self.assertEqual(num_comm_div(1050, 1100), 2)

    def test_edge_case35(self):
        self.assertEqual(num_comm_div(1100, 1150), 2)

    def test_edge_case36(self):
        self.assertEqual(num_comm_div(1150, 1200), 2)

    def test_edge_case37(self):
        self.assertEqual(num_comm_div(1200, 1250), 2)

    def test_edge_case38(self):
        self.assertEqual(num_comm_div(1250, 1300), 2)

    def test_edge_case39(self):
        self.assertEqual(num_comm_div(1300, 1350), 2)

    def test_edge_case40(self):
        self.assertEqual(num_comm_div(1350, 1400), 2)

    def test_edge_case41(self):
        self.assertEqual(num_comm_div(1400, 1450), 2)

    def test_edge_case42(self):
        self.assertEqual(num_comm_div(1450