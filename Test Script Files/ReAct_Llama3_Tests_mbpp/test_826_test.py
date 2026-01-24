import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):
    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(7, 8, 1), "Obtuse-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Acute-angled Triangle")

    def test_equal_sides(self):
        with self.assertRaises(ZeroDivisionError):
            check_Type_Of_Triangle(0, 0, 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", "b", "c")

    def test_zero_sides(self):
        with self.assertRaises(ZeroDivisionError):
            check_Type_Of_Triangle(0, 0, 5)

    def test_negative_sides(self):
        self.assertEqual(check_Type_Of_Triangle(-3, 4, 5), "Acute-angled Triangle")

    def test_zero_and_negative_sides(self):
        with self.assertRaises(ZeroDivisionError):
            check_Type_Of_Triangle(0, -3, 5)
