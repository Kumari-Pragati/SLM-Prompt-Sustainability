import unittest
from mbpp_17_code import square_perimeter

class TestSquarePerimeter(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_zero_case(self):
        self.assertEqual(square_perimeter(0), 0)

    def test_negative_case(self):
        with self.assertRaises(Exception):
            square_perimeter(-5)

    def test_large_number_case(self):
        self.assertEqual(square_perimeter(10000), 40000)
