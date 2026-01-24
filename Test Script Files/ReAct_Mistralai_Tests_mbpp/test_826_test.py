import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        # Typical case: Right-angled triangle with sides 3-4-5
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_right_angled_triangle_with_zero(self):
        # Edge case: Right-angled triangle with one side as zero
        self.assertRaises(ValueError, check_Type_Of_Triangle, 0, 4, 5)

    def test_right_angled_triangle_with_negative(self):
        # Edge case: Right-angled triangle with negative sides
        self.assertRaises(ValueError, check_Type_Of_Triangle, -3, 4, 5)

    def test_acute_angled_triangle(self):
        # Typical case: Acute-angled triangle with sides 2-3-4
        self.assertEqual(check_Type_Of_Triangle(2, 3, 4), "Acute-angled Triangle")

    def test_obtuse_angled_triangle(self):
        # Typical case: Obtuse-angled triangle with sides 5-3-4
        self.assertEqual(check_Type_Of_Triangle(5, 3, 4), "Obtuse-angled Triangle")

    def test_degenerate_triangle(self):
        # Edge case: Degenerate triangle (two sides equal)
        self.assertRaises(ValueError, check_Type_Of_Triangle, 3, 3, 3)

    def test_invalid_triangle(self):
        # Edge case: Invalid triangle (sum of sides less than the largest side)
        self.assertRaises(ValueError, check_Type_Of_Triangle, 2, 2, 3)
