import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Obtuse-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Acute-angled Triangle")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", "b", "c")

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle(1, "b", 3)

    def test_zero_side(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle(0, 3, 4)

    def test_negative_side(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle(-1, 3, 4)

    def test_equal_sides(self):
        self.assertEqual(check_Type_Of_Triangle(3, 3, 4), "Acute-angled Triangle")

    def test_all_equal_sides(self):
        self.assertEqual(check_Type_Of_Triangle(3, 3, 3), "Acute-angled Triangle")
