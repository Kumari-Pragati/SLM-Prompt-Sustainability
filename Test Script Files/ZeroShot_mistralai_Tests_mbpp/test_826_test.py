import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(7, 24, 25), "Right-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(6, 4, 8), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(12, 16, 20), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(15, 12, 13), "Obtuse-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(4, 3, 5), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Acute-angled Triangle")
