import unittest
from mbpp_799_code import left_Rotate

class TestLeftRotate(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(left_Rotate(10, 2), 40)

    def test_boundary_case(self):
        self.assertEqual(left_Rotate(0, 32), 0)
        self.assertEqual(left_Rotate(2147483647, 1), 2147483648)

    def test_edge_case(self):
        self.assertEqual(left_Rotate(2147483647, 0), 2147483647)
        self.assertEqual(left_Rotate(2147483647, 32), 2147483647)
        self.assertEqual(left_Rotate(2147483647, 33), 0)
