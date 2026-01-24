import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):
    def test_right_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_acute_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(2, 3, 4), "Acute-angled Triangle")

    def test_obtuse_angled_triangle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Obtuse-angled Triangle")

    def test_invalid_input_a(self):
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(-1, 2, 3)

    def test_invalid_input_b(self):
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(2, -1, 3)

    def test_invalid_input_c(self):
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(2, 3, -1)

    def test_degenerate_triangle(self):
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(0, 0, 0)
