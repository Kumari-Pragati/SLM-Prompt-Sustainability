import unittest
from mbpp_215_code import decode_list

class TestDecodeList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(decode_list([[1, 2], [3, 4]]), [(2, range(1)), (4, range(1))])

    def test_edge_case(self):
        self.assertEqual(decode_list([[1, 2], [3]]), [(2, range(1)), (3, [0])])

    def test_edge_case2(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5]]), [(2, range(1)), (4, range(1)), (5, [0])])

    def test_edge_case3(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6]]), [(2, range(1)), (4, range(1)), (6, [0])])

    def test_edge_case4(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7]]), [(2, range(1)), (4, range(1)), (6, range(1)), (7, [0])])

    def test_edge_case5(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7, 8]]), [(2, range(1)), (4, range(1)), (6, range(1)), (8, [0])])

    def test_edge_case6(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7, 8, 9]]), [(2, range(1)), (4, range(1)), (6, range(1)), (8, range(1)), (9, [0])])

    def test_edge_case7(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7, 8, 9, 10]]), [(2, range(1)), (4, range(1)), (6, range(1)), (8, range(1)), (10, [0])])

    def test_edge_case8(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11]]), [(2, range(1)), (4, range(1)), (6, range(1)), (8, range(1)), (10, range(1)), (11, [0])])

    def test_edge_case9(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]), [(2, range(1)), (4, range(1)), (6, range(1)), (8, range(1)), (10, range(1)), (12, [0])])

    def test_edge_case10(self):
        self.assertEqual(decode_list([[1, 2], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]), [(2, range(1)), (4, range(1)), (6, range(1)), (8, range(1)), (10, range(1)), (12, range(1)), (13, [0])])
