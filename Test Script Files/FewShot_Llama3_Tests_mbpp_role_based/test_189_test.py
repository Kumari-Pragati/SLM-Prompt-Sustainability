import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    def test_first_missing_positive(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4], 4), 5)

    def test_first_missing_positive_edge_case(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5], 5), 6)

    def test_first_missing_positive_edge_case2(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 5, 6], 6), 4)

    def test_first_missing_positive_edge_case3(self):
        self.assertEqual(first_Missing_Positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 11)

    def test_first_missing_positive_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive("hello", 4)

    def test_first_missing_positive_invalid_input2(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive([1, 2, 3], "hello")
