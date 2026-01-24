import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3)))
        self.assertEqual(substract_elements((0, 0, 0), (0, 0, 0)), ((0, 0, 0)))

    def test_edge_cases(self):
        self.assertEqual(substract_elements((1, 2, 3), (0, 0, 0)), ((1, 2, 3)))
        self.assertEqual(substract_elements((0, 0, 0), (1, 2, 3)), ((-1, -2, -3)))
        self.assertEqual(substract_elements((1, 2, 3), (4, 4, 4)), ((-3, -2, -1)))
        self.assertEqual(substract_elements((4, 4, 4), (1, 2, 3)), ((3, 2, 1)))

    def test_complex(self):
        self.assertEqual(substract_elements((1, 2, 3), (3, 2, 1)), ((-2, -1, -3)))
        self.assertEqual(substract_elements((-1, -2, -3), (1, 2, 3)), ((-2, -3, -4)))
        self.assertEqual(substract_elements((-1, 0, 1), (1, -1, 0)), ((0, 1, 1)))
