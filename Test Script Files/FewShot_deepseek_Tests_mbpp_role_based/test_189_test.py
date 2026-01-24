import unittest
from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(first_Missing_Positive([1,2,0], 3), 3)

    def test_typical_case_2(self):
        self.assertEqual(first_Missing_Positive([3,4,-1,1], 4), 2)

    def test_typical_case_3(self):
        self.assertEqual(first_Missing_Positive([7,8,9,10], 4), 1)

    def test_boundary_condition_1(self):
        self.assertEqual(first_Missing_Positive([], 0), 1)

    def test_boundary_condition_2(self):
        self.assertEqual(first_Missing_Positive([1], 1), 2)

    def test_boundary_condition_3(self):
        self.assertEqual(first_Missing_Positive([2], 1), 1)

    def test_edge_case_1(self):
        self.assertEqual(first_Missing_Positive([1,1,1,1], 4), 2)

    def test_edge_case_2(self):
        self.assertEqual(first_Missing_Positive([-1,-1,-1,-1], 4), 1)

    def test_edge_case_3(self):
        self.assertEqual(first_Missing_Positive([-1,0,1,2], 4), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive("not a list", 0)
