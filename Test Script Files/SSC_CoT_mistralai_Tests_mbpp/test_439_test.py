import unittest
from mbpp_439_code import multiple_to_single

class TestMultipleToSingle(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5]), 12345)
        self.assertEqual(multiple_to_single([0, 0, 0, 0, 0]), 0)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5, 6]), 123456)
        self.assertEqual(multiple_to_single([1, 2, 3, 4, 5, 6, 7, 8, 9]), 123456789)
        self.assertEqual(multiple_to_single([10, 20, 30, 40, 50]), 123450)
        self.assertEqual(multiple_to_single([-1, -2, -3, -4, -5]), 12345)
        self.assertEqual(multiple_to_single([0, 0, 0, 0, 9]), 9)
        self.assertEqual(multiple_to_single([9, 0, 0, 0, 0]), 9)

    def test_special_cases(self):
        self.assertEqual(multiple_to_single([0, 0, 0, 0, 1]), 1)
        self.assertEqual(multiple_to_single([1, 0, 0, 0, 0]), 1)
        self.assertEqual(multiple_to_single([0, 1, 0, 0, 0]), 1)
        self.assertEqual(multiple_to_single([0, 0, 1, 0, 0]), 1)
        self.assertEqual(multiple_to_single([0, 0, 0, 1, 0]), 1)
