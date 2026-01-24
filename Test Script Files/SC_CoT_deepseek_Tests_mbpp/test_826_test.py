import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Obtuse-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Acute-angled Triangle")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", 4, 5)

    def test_boundary_conditions(self):
        self.assertEqual(check_Type_Of_Triangle(0, 0, 0), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1.414), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1.732), "Obtuse-angled Triangle")
