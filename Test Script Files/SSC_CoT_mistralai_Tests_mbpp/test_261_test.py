import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertTupleEqual(division_elements((2, 4, 6), (1, 2, 3)), (0, 1, 2))
        self.assertTupleEqual(division_elements((-2, 4, -6), (1, 2, -3)), (-1, 2, 2))
        self.assertTupleEqual(division_elements((0, 0, 0), (1, 2, 3)), (0, 0, 0))

    def test_edge_and_boundary_conditions(self):
        self.assertRaises(TypeError, division_elements, (1,), (2,))
        self.assertRaises(TypeError, division_elements, (1, 2), ())
        self.assertRaises(TypeError, division_elements, (1, 2.5), (2,))
        self.assertRaises(TypeError, division_elements, (1, 2), (0,))
        self.assertRaises(TypeError, division_elements, (1, 2), (-1,))
        self.assertRaises(TypeError, division_elements, (0, 2), (0,))
        self.assertRaises(TypeError, division_elements, (1, 0), (2,))
        self.assertTupleEqual(division_elements((1, 0), (0, 1)), (0, None))
        self.assertTupleEqual(division_elements((1, -1), (0, 1)), (1, -1))
