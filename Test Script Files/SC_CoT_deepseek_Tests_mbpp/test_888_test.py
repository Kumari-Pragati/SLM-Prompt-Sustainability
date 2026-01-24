import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))

    def test_edge_case(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), ((0, 0, 0),))

    def test_boundary_case(self):
        self.assertEqual(substract_elements((1000, 2000, 3000), (-1000, -2000, -3000)), ((2000, 4000, 6000),))

    def test_special_case(self):
        self.assertEqual(substract_elements((10, 20, 30), (10, 20, 30)), ((0, 0, 0),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), "abc")
