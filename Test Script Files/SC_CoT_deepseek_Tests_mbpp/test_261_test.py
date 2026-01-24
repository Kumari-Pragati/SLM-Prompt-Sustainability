import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(division_elements((10, 20), (2, 4)), ((5, 5)))

    def test_boundary_case(self):
        self.assertEqual(division_elements((0, 20), (2, 4)), ((0, 5)))

    def test_edge_case(self):
        self.assertEqual(division_elements((10, 0), (2, 0)), ((5, 'Error')))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            division_elements((10, 20), '2, 4')
