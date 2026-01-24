import unittest
from mbpp_233_code import lateralsuface_cylinder

class TestLateralsufaceCylinder(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(5, 10), 785.3981633974483)

    def test_edge_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(0, 10), 0)
        self.assertAlmostEqual(lateralsuface_cylinder(5, 0), 0)

    def test_boundary_case(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 10), 6283.185307179586)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('a', 10)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder(5, 'b')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            lateralsuface_cylinder('a', 'b')
