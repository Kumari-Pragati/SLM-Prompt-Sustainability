import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_edge_case(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 6], 5), 5)

    def test_edge_case2(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 7], 5), 6)

    def test_edge_case3(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 8], 5), 7)

    def test_edge_case4(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8], 5), 9)

    def test_edge_case5(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9], 5), 10)

    def test_edge_case6(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 11)

    def test_edge_case7(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 5), 12)

    def test_edge_case8(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 5), 13)

    def test_edge_case9(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 5), 14)

    def test_edge_case10(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 5), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive("test", 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive([1, 2, 3, 4, 5], "test")

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive([1, 2, 3, 4, 5], 5.5)

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive([1, 2, 3, 4, 5], -5)

    def test_invalid_input5(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive([1, 2, 3, 4, 5], 0)
