import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5], 5), 6)

    def test_edge_case(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6], 6), 7)

    def test_edge_case2(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7], 7), 8)

    def test_edge_case3(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8], 8), 9)

    def test_edge_case4(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9], 9), 10)

    def test_edge_case5(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10], 10), 11)

    def test_edge_case6(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11], 11), 12)

    def test_edge_case7(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12], 12), 13)

    def test_edge_case8(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13], 13), 14)

    def test_edge_case9(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14], 14), 15)

    def test_edge_case10(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 15), 16)

    def test_edge_case11(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], 16), 17)

    def test_edge_case12(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 17), 18)

    def test_edge_case13(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 18), 19)

    def test_edge_case14(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], 19), 20)

    def test_edge_case15(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 20), 21)

    def test_edge_case16(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21], 21), 22)

    def test_edge_case17(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22], 22), 23)

    def test_edge_case18(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], 23), 24)

    def test_edge_case19(self):
        self.assertEqual(first_Missing_Positive([1,2,3,4,5,6,7,8