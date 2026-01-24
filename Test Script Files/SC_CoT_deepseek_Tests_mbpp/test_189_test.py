import unittest

from mbpp_189_code import first_Missing_Positive

class TestFirstMissingPositive(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(first_Missing_Positive([3, 4, -1, 1], 4), 2)

    def test_edge_case(self):
        self.assertEqual(first_Missing_Positive([1, 2, 0], 3), 3)

    def test_boundary_case(self):
        self.assertEqual(first_Missing_Positive([-8, -7, -6], 3), 1)

    def test_special_case(self):
        self.assertEqual(first_Missing_Positive([2, 3, 4, 5, 6], 5), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            first_Missing_Positive("not a list", 0)
