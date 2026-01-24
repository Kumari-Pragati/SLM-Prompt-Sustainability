import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(multiple_to_single([1, 2, 3]), 123)

    def test_edge_boundary_conditions(self):
        self.assertEqual(multiple_to_single([0]), 0)
        self.assertEqual(multiple_to_single([9]), 9)
        self.assertEqual(multiple_to_single([9, 9]), 99)
        self.assertEqual(multiple_to_single([0, 0]), 0)
        self.assertEqual(multiple_to_single([-1, -2, -3]), -123)
        self.assertEqual(multiple_to_single([-9]), -9)
        self.assertEqual(multiple_to_single([-9, -9]), -99)
        self.assertEqual(multiple_to_single([0, -1]), 0)

    def test_more_complex_cases(self):
        self.assertEqual(multiple_to_single([10, 20, 30]), 102030)
        self.assertEqual(multiple_to_single([-10, -20, -30]), -102030)
        self.assertEqual(multiple_to_single([99, 99]), 9999)
        self.assertEqual(multiple_to_single([0, 0, 0]), 0)
        self.assertEqual(multiple_to_single([9, 9, 9, 9]), 9999)
