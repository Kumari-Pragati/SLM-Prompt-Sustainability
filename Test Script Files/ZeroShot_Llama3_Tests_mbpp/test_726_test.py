import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_multiply_elements(self):
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 3, 6))
        self.assertEqual(multiply_elements((4, 5, 6)), (20, 30, 36))
        self.assertEqual(multiply_elements((-1, 2, 3)), (-2, 6, 9))
        self.assertEqual(multiply_elements((0, 0, 0)), (0, 0, 0))
        self.assertEqual(multiply_elements((-1, -2, -3)), (2, 6, 9))

    def test_multiply_elements_empty(self):
        with self.assertRaises(IndexError):
            multiply_elements(())

    def test_multiply_elements_single(self):
        with self.assertRaises(IndexError):
            multiply_elements((1,))
