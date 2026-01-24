import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(substract_elements((5, 3, 2), (1, 2, 1)), (4, 1, 1))

    def test_edge_conditions(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))
        self.assertEqual(substract_elements((10, 20, 30), (10, 20, 30)), (0, 0, 0))

    def test_boundary_conditions(self):
        self.assertEqual(substract_elements((-100, 100, 0), (-100, 100, 0)), (0, 0, 0))
        self.assertEqual(substract_elements((100, -100, 0), (100, -100, 0)), (0, 0, 0))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), 4)
        with self.assertRaises(TypeError):
            substract_elements(4, (1, 2, 3))
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 'a'), (1, 2, 3))
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), (1, 2, 'a'))
