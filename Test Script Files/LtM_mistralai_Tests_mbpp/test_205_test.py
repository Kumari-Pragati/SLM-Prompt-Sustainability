import unittest
from mbpp_205_code import inversion_elements

class TestInversionElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(inversion_elements((1, 0, 1)), (0, 1, 0))
        self.assertEqual(inversion_elements((0, 1, 0)), (1, 0, 1))
        self.assertEqual(inversion_elements((1, 1, 1)), (0, 0, 0))

    def test_edge_and_boundary(self):
        self.assertEqual(inversion_elements((0,)), (1,))
        self.assertEqual(inversion_elements((1, 0, 1, 0)), (0, 1, 1, 0))
        self.assertEqual(inversion_elements((-1, 0, 1)), (0, 1, ~-1))

    def test_complex(self):
        self.assertEqual(inversion_elements((1, 0, 1, 0, 1, 0)), (0, 1, 1, 0, 0, 1))
        self.assertEqual(inversion_elements((1, -1, 1)), (0, ~-1, 1))
        self.assertEqual(inversion_elements((1, 0, -1)), (0, 1, ~-1))
