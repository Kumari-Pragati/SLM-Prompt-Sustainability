import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)
        self.assertEqual(multiple_to_single([0, 0, 0]), 0)
        self.assertEqual(multiple_to_single([9, 8, 7]), 987)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(multiple_to_single([]), 0)
        self.assertEqual(multiple_to_single([10]), 10)
        self.assertEqual(multiple_to_single([9, 9, 9]), 729)
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)

    def test_complex_inputs(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 0, 0]), 12300)
        self.assertEqual(multiple_to_single([0, 0, 1, 2, 3]), 123)
        self.assertEqual(multiple_to_single([9, 8, 7, 6, 5]), 98765)
        self.assertEqual(multiple_to_single([-1, -2, -3, 0, 0]), -12300)
