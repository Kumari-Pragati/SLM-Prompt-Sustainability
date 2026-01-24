import unittest
from mbpp_390_code import add_string

class TestAddString(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(add_string([1, 2, 3], "{}"), ['1', '2', '3'])
        self.assertEqual(add_string(["a", "b", "c"], "{}"), ['a', 'b', 'c'])
        self.assertEqual(add_string([1.5, 2.7, 3.1], "{:.1f}"), ['1.5', '2.7', '3.1'])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(add_string([], "{}"), [])
        self.assertEqual(add_string([None], "{}"), ['None'])
        self.assertEqual(add_string([1, 2, 3, 4], "{}"), ['1', '2', '3', '4'])
        self.assertEqual(add_string([1, 2, 3, 4, 5], "{}"), ['1', '2', '3', '4', '5'])
        self.assertEqual(add_string([1, 2, 3, 4, 5, 6], "{}"), ['1', '2', '3', '4', '5', '6'])

    def test_format_string_with_placeholders(self):
        self.assertEqual(add_string([1, 2, 3], "{} {:^3} {}"), ['1', ' 2  ', '3'])
        self.assertEqual(add_string([1, 2, 3], "{} {:03} {}"), ['1', '002', '003'])
        self.assertEqual(add_string([1, 2, 3], "{} {:.2f} {}", [1.5, 2.7, 3.1]), ['1.00', '2.70', '3.10'])

    def test_invalid_input(self):
        self.assertRaises(TypeError, lambda: add_string("list", "string"))
        self.assertRaises(TypeError, lambda: add_string([1], 2))
