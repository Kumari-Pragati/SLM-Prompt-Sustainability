import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(max_of_three(3, 2, 1), 3)
        self.assertEqual(max_of_three(2, 3, 1), 3)
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(2, 2, 3), 3)
        self.assertEqual(max_of_three(2, 3, 2), 3)

    def test_edge_cases(self):
        self.assertEqual(max_of_three(0, 0, 1), 1)
        self.assertEqual(max_of_three(1, 0, 0), 1)
        self.assertEqual(max_of_three(-1, -2, -3), -1)
        self.assertEqual(max_of_three(-2, -1, -3), -1)
        self.assertEqual(max_of_three(-3, -2, -1), -1)

    def test_boundary_cases(self):
        self.assertEqual(max_of_three(sys.maxsize, 0, -1), sys.maxsize)
        self.assertEqual(max_of_three(0, sys.maxsize, -1), sys.maxsize)
        self.assertEqual(max_of_three(-1, sys.maxsize, 0), sys.maxsize)
        self.assertEqual(max_of_three(sys.maxsize, sys.maxsize, 0), sys.maxsize)
        self.assertEqual(max_of_three(0, sys.maxsize, sys.maxsize), sys.maxsize)
