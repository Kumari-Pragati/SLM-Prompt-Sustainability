import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_multiply_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3, 4)), (2, 6, 12))
        self.assertEqual(multiply_elements((5, 5, 5)), (25,))
        self.assertEqual(multiply_elements((10, 20, 30, 40, 50)), (200, 600, 1200, 2000))
        self.assertEqual(multiply_elements(()), ())
        self.assertEqual(multiply_elements((1,)), ())
