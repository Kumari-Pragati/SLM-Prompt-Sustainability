import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(division_elements((10, 20), (2, 4)), ((5, 5)))

    def test_edge_case(self):
        self.assertEqual(division_elements((0, 10), (2, 0)), ((0, 0)))

    def test_boundary_case(self):
        self.assertEqual(division_elements((10, 20), (1, 2)), ((10, 10)))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            division_elements((10, 20), (2, 'a'))
