import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)
        self.assertEqual(median_numbers(3, 2, 1), 2)
        self.assertEqual(median_numbers(2, 3, 1), 2)

    def test_edge_cases(self):
        self.assertEqual(median_numbers(1, 1, 1), 1)
        self.assertEqual(median_numbers(2, 1, 1), 1.5)
        self.assertEqual(median_numbers(1, 2, 2), 2)
        self.assertEqual(median_numbers(-1, -2, -3), -1.5)
        self.assertEqual(median_numbers(0, 0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(median_numbers(sys.maxsize, sys.maxsize, sys.maxsize), sys.maxsize)
        self.assertEqual(median_numbers(-sys.maxsize, -sys.maxsize, -sys.maxsize), -sys.maxsize)
        self.assertEqual(median_numbers(sys.maxsize, -sys.maxsize, sys.maxsize), sys.maxsize/2)
        self.assertEqual(median_numbers(-sys.maxsize, sys.maxsize, -sys.maxsize), -sys.maxsize/2)
