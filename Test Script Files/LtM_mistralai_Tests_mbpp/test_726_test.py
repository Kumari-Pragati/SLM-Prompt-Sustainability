import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 3))
        self.assertEqual(multiply_elements((4, 5, 6)), (0, 5, 6))
        self.assertEqual(multiply_elements((7, 8, 9)), (0, 8, 9))

    def test_edge_cases(self):
        self.assertEqual(multiply_elements((1,)), ())
        self.assertEqual(multiply_elements((1)), ())
        self.assertEqual(multiply_elements((1, 2)), ())
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 3, 0, 4))
