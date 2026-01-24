import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertTupleEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-4, -3, -3)))
        self.assertTupleEqual(substract_elements((0, 0, 0), (1, 2, 3)), ((-1, -2, -3)))
        self.assertTupleEqual(substract_elements((10, 20, 30), (50, 40, 30)), ((-40, -20, 0)))

    def test_edge_and_boundary_conditions(self):
        self.assertTupleEqual(substract_elements((1, 2, 3), (0, 0, 0)), ((1, 2, 3)))
        self.assertTupleEqual(substract_elements((0, 0, 0), (1, 2, 3)), ((-1, -2, -3)))
        self.assertTupleEqual(substract_elements((1, 2, 3), (-1, -2, -3)), ((2, 4, 6)))
        self.assertTupleEqual(substract_elements((-1, -2, -3), (1, 2, 3)), ((-2, -4, -6)))
        self.assertTupleEqual(substract_elements((-1, -2, -3), (-1, -2, -3)), ((0, 0, 0)))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, substract_elements, (1, 2, 3), 'not a tuple')
        self.assertRaises(TypeError, substract_elements, 'not a tuple', (1, 2, 3))
        self.assertRaises(ValueError, substract_elements, (1, 2, 3, 4), (1, 2, 3))
        self.assertRaises(ValueError, substract_elements, (1, 2, 3), (1, 2, 3, 4))
