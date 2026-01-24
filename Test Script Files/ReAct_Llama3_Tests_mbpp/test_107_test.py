import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start(self):
        self.assertEqual(count_Hexadecimal(15, 15), 1)

    def test_edge_case_end(self):
        self.assertEqual(count_Hexadecimal(16, 20), 2)

    def test_edge_case_start_end(self):
        self.assertEqual(count_Hexadecimal(15, 16), 1)

    def test_edge_case_start_end_reverse(self):
        self.assertEqual(count_Hexadecimal(16, 15), 1)

    def test_edge_case_start_end_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(15, 10), 0)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count_Hexadecimal(10, 15), 6)

    def test_edge_case_start_end_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(count