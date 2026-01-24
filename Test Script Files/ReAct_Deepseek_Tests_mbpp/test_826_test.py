import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Obtuse-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Acute-angled Triangle")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", "b", "c")

    def test_zero_or_negative_input(self):
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(0, 2, 3)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle(1.5, 2, 3)
