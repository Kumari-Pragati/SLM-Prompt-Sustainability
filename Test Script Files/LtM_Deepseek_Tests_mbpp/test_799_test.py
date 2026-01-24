import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(left_Rotate(1, 1), 2)
        self.assertEqual(left_Rotate(10, 2), 40)

    def test_boundary_conditions(self):
        self.assertEqual(left_Rotate(0, 10), 0)
        self.assertEqual(left_Rotate(2147483647, 1), 2147483648)

    def test_edge_cases(self):
        self.assertEqual(left_Rotate(1, 32), 1)
        self.assertEqual(left_Rotate(1, 0), 1)
        self.assertEqual(left_Rotate(2147483647, 31), 2147483647)

    def test_complex_cases(self):
        self.assertEqual(left_Rotate(15, 10), 1280)
        self.assertEqual(left_Rotate(40, 20), 160)
