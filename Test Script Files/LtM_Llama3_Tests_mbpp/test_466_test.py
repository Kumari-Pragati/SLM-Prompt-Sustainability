import unittest
from mbpp_466_code import find_peak

class TestFindPeak(unittest.TestCase):
    def test_simple_peak(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5], 5), 4)

    def test_edge_case_peak(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6], 6), 5)

    def test_edge_case_peak2(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7], 7), 6)

    def test_edge_case_peak3(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8], 8), 7)

    def test_edge_case_peak4(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 8)

    def test_edge_case_peak5(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 9)

    def test_edge_case_peak6(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 10)

    def test_edge_case_peak7(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 12), 11)

    def test_edge_case_peak8(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 13), 12)

    def test_edge_case_peak9(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 14), 13)

    def test_edge_case_peak10(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 15), 14)

    def test_edge_case_peak11(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 16), 15)

    def test_edge_case_peak12(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 17), 16)

    def test_edge_case_peak13(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 18), 17)

    def test_edge_case_peak14(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 19), 18)

    def test_edge_case_peak15(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20), 19)

    def test_edge_case_peak16(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21], 21), 20)

    def test_edge_case_peak