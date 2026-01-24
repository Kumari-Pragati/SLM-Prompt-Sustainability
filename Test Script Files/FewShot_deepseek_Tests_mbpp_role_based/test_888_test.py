import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))

    def test_edge_conditions(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), ((0, 0, 0),))
        self.assertEqual(substract_elements((10, 20, 30), (10, 20, 30)), ((0, 0, 0),))

    def test_boundary_conditions(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))
        self.assertEqual(substract_elements((-1, -2, -3), (4, 5, 6)), ((-5, -7, -9),))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), "4, 5, 6")
        with self.assertRaises(TypeError):
            substract_elements("1, 2, 3", (4, 5, 6))
        with self.assertRaises(TypeError):
            substract_elements("1, 2, 3", "4, 5, 6")
