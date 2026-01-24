import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((10, 20, 30), (5, 10, 15)), (5, 10, 15))

    def test_edge_case(self):
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), (0, 0, 0))

    def test_boundary_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (0, 0, 0)), (1, 2, 3))
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), (-1, -2, -3))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            substract_elements((1, 2, 3), "abc")
