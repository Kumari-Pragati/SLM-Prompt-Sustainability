import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(num_comm_div(12, 15), 2)

    def test_edge_case(self):
        self.assertEqual(num_comm_div(1, 1), 2)

    def test_edge_case2(self):
        self.assertEqual(num_comm_div(2, 3), 2)

    def test_edge_case3(self):
        self.assertEqual(num_comm_div(3, 4), 2)

    def test_edge_case4(self):
        self.assertEqual(num_comm_div(4, 6), 2)

    def test_edge_case5(self):
        self.assertEqual(num_comm_div(5, 6), 2)

    def test_edge_case6(self):
        self.assertEqual(num_comm_div(6, 8), 2)

    def test_edge_case7(self):
        self.assertEqual(num_comm_div(7, 8), 2)

    def test_edge_case8(self):
        self.assertEqual(num_comm_div(8, 9), 2)

    def test_edge_case9(self):
        self.assertEqual(num_comm_div(9, 10), 2)

    def test_edge_case10(self):
        self.assertEqual(num_comm_div(10, 12), 2)

    def test_edge_case11(self):
        self.assertEqual(num_comm_div(11, 12), 2)

    def test_edge_case12(self):
        self.assertEqual(num_comm_div(12, 13), 2)

    def test_edge_case13(self):
        self.assertEqual(num_comm_div(13, 14), 2)

    def test_edge_case14(self):
        self.assertEqual(num_comm_div(14, 15), 2)

    def test_edge_case15(self):
        self.assertEqual(num_comm_div(15, 16), 2)

    def test_edge_case16(self):
        self.assertEqual(num_comm_div(16, 17), 2)

    def test_edge_case17(self):
        self.assertEqual(num_comm_div(17, 18), 2)

    def test_edge_case18(self):
        self.assertEqual(num_comm_div(18, 19), 2)

    def test_edge_case19(self):
        self.assertEqual(num_comm_div(19, 20), 2)

    def test_edge_case20(self):
        self.assertEqual(num_comm_div(20, 21), 2)
