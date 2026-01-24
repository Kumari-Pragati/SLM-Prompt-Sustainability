import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsufaceCylinder(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(lateralsuface_cylinder(1, 2), 12.56636)

    def test_edge_case_zero_radius(self):
        self.assertEqual(lateralsuface_cylinder(0, 2), 0)

    def test_edge_case_zero_height(self):
        self.assertEqual(lateralsuface_cylinder(1, 0), 0)

    def test_edge_case_negative_radius(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(-1, 2)

    def test_edge_case_negative_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(1, -2)

    def test_edge_case_non_numeric_radius(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('a', 2)

    def test_edge_case_non_numeric_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(1, 'b')

    def test_edge_case_non_numeric_radius_and_height(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('a', 'b')

    def test_edge_case_max_radius(self):
        self.assertEqual(lateralsuface_cylinder(1e308, 2), 1e308*3.1415*2)

    def test_edge_case_max_height(self):
        self.assertEqual(lateralsuface_cylinder(1, 1e308), 1e308*3.1415*1)

    def test_edge_case_min_radius(self):
        self.assertEqual(lateralsuface_cylinder(1e-308, 2), 1e-308*3.1415*2)

    def test_edge_case_min_height(self):
        self.assertEqual(lateralsuface_cylinder(1, 1e-308), 1e-308*3.1415*1)
