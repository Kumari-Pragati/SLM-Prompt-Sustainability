import unittest
from mbpp_51_code import check_equilateral

class TestCheckEquilateral(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_equilateral(3, 3, 3))

    def test_edge_case(self):
        self.assertTrue(check_equilateral(0, 0, 0))

    def test_boundary_case(self):
        self.assertTrue(check_equilateral(1, 1, 1))
        self.assertTrue(check_equilateral(2, 2, 2))
        self.assertTrue(check_equilateral(100, 100, 100))

    def test_corner_case(self):
        self.assertTrue(check_equilateral(float('inf'), float('inf'), float('inf')))
        self.assertTrue(check_equilateral(-float('inf'), -float('inf'), -float('inf')))

    def test_invalid_input(self):
        self.assertFalse(check_equilateral('a', 'a', 'a'))
        self.assertFalse(check_equilateral(None, None, None))
        self.assertFalse(check_equilateral([1, 2, 3], [1, 2, 3], [1, 2, 3]))
