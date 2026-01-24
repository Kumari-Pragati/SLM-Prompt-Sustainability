import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Right-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 6), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1), "Acute-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(6, 4, 5), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(10, 12, 15), "Obtuse-angled Triangle")

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, check_Type_Of_Triangle, 0, 0, 0)
        self.assertRaises(ValueError, check_Type_Of_Triangle, -1, 2, 3)
        self.assertRaises(ValueError, check_Type_Of_Triangle, 1, -2, 3)
        self.assertRaises(ValueError, check_Type_Of_Triangle, 1, 2, -3)
