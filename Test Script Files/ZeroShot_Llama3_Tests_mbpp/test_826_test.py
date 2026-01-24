import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_right_angle(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")

    def test_obtuse_angle(self):
        self.assertEqual(check_Type_Of_Triangle(7, 24, 25), "Obtuse-angled Triangle")

    def test_acute_angle(self):
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Acute-angled Triangle")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Type_Of_Triangle("a", "b", "c")

    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            check_Type_Of_Triangle(0, 0, 0)
