import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_no_triangle(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_yes_triangle(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')

    def test_no_triangle_negative(self):
        self.assertEqual(check_Triangle(-1,-1,-2,-2,-3,-3), 'No')

    def test_yes_triangle_negative(self):
        self.assertEqual(check_Triangle(-1,-1,0,0,1,1), 'Yes')

    def test_no_triangle_zero(self):
        self.assertEqual(check_Triangle(0,0,0,0,0,0), 'No')

    def test_yes_triangle_zero(self):
        self.assertEqual(check_Triangle(0,0,1,1,2,2), 'Yes')
