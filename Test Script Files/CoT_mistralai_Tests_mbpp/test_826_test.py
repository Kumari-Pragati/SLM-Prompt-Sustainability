import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(12, 16, 20), "Right-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(15, 36, 39), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(24, 60, 65), "Obtuse-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5.1), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(6, 8, 9.5), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(12, 16, 17), "Acute-angled Triangle")

    def test_invalid_input(self):
        self.assertRaises(ValueError, check_Type_Of_Triangle, 0, 0, 0)
        self.assertRaises(ValueError, check_Type_Of_Triangle, -1, 2, 3)
        self.assertRaises(ValueError, check_Type_Of_Triangle, 1, -2, 3)
