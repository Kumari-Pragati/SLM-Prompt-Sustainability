import unittest
from mbpp_826_code import check_Type_Of_Triangle

class TestCheckTypeOfTriangle(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(check_Type_Of_Triangle(3, 4, 5), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(6, 8, 10), "Right-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(5, 12, 13), "Right-angled Triangle")

    def test_edge_conditions(self):
        self.assertEqual(check_Type_Of_Triangle(0, 0, 0), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(1, 1, 1), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(2, 2, 2), "Acute-angled Triangle")

    def test_complex_cases(self):
        self.assertEqual(check_Type_Of_Triangle(7, 7, 7), "Acute-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(10, 24, 26), "Obtuse-angled Triangle")
        self.assertEqual(check_Type_Of_Triangle(15, 20, 30), "Obtuse-angled Triangle")
