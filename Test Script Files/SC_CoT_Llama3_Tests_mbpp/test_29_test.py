import unittest
from mbpp_29_code import get_Odd_Occurrence

class TestGetOddOccurrence(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 2, 2, 3], 5), 1)

    def test_edge_case2(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 3, 4], 5), 1)

    def test_edge_case3(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5], 5), 1)

    def test_edge_case4(self):
        self.assertEqual(get_Odd_Occurrence([1, 1, 1, 1, 1], 5), 1)

    def test_edge_case5(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6], 6), 1)

    def test_edge_case6(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7], 7), 1)

    def test_edge_case7(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8], 8), 1)

    def test_edge_case8(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 1)

    def test_edge_case9(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 1)

    def test_edge_case10(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 1)

    def test_edge_case11(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 1)

    def test_edge_case12(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 1)

    def test_edge_case13(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 1)

    def test_edge_case14(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 1)

    def test_edge_case15(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 1)

    def test_edge_case16(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 1)

    def test_edge_case17(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 1)

    def test_edge_case18(self):
        self.assertEqual(get_Odd_Occurrence([1, 2, 3, 4, 5, 6, 7, 8, 9,