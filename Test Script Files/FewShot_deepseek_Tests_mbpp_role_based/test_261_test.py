import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(division_elements((10, 20), (2, 4)), ((5, 5)))

    def test_edge_conditions(self):
        self.assertEqual(division_elements((0, 0), (2, 4)), ((0, 0)))

    def test_boundary_conditions(self):
        self.assertEqual(division_elements((1, 2, 3), (1, 2, 3)), ((1, 1, 1)))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            division_elements((10, 20), 2)
