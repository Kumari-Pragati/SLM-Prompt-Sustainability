import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_positive_case(self):
        self.assertEqual(check_Triangle(0, 0, 3, 4, 1, 1), 'Yes')

    def test_negative_case(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 2, 2), 'No')

    def test_zero_case(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')

    def test_negative_and_positive_case(self):
        self.assertEqual(check_Triangle(-1, -1, 1, 1, 0, 0), 'Yes')
