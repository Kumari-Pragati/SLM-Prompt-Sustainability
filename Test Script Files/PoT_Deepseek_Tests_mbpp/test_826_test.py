import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(7, 24, 25), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(8, 15, 17), "Right-angled Triangle")

    def test_edge_cases(self):
        self.assertEqual(check_Type_Of_Triangle(0, 0, 0), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 2), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 2, 3), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 2, 2.4), "Obtuse-angled Triangle")

    def test_boundary_cases(self):
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1.4142135623730951), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1.4142135623730952), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1.4142135623730953), "Obtuse-angled Triangle")
