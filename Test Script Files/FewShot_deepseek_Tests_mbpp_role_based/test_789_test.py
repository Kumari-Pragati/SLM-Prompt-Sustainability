import unittest
from mbpp_789_code import perimeter_polygon

class TestPerimeterPolygon(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(perimeter_polygon(4, 5), 20)

    def test_boundary_conditions(self):
        self.assertEqual(perimeter_polygon(0, 5), 0)
        self.assertEqual(perimeter_polygon(4, 0), 0)

    def test_edge_conditions(self):
        self.assertEqual(perimeter_polygon(1000000, 1), 1000000)
        self.assertEqual(perimeter_polygon(1, 1000000), 1000000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter_polygon("4", 5)
        with self.assertRaises(TypeError):
            perimeter_polygon(4, "5")
        with self.assertRaises(TypeError):
            perimeter_polygon("4", "5")
