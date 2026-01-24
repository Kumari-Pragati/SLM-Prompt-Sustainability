import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):
    def test_acute_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Acute-angled Triangle")

    def test_right_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_obtuse_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Obtuse-angled Triangle")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", 4, 5)

    def test_zero_sides(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle(0, 4, 5)

    def test_negative_sides(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle(-1, 4, 5)

    def test_non_numeric_sides(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", "b", "c")
