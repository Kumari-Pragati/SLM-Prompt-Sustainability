import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5, 6)), ((-3, -3, -3),))

    def test_edge_case(self):
        self.assertEqual(substract_elements((1, 2), (3, 4)), ((-2, -2),))

    def test_edge_case2(self):
        self.assertEqual(substract_elements((1, 2, 3), ()), ((1, 2, 3),))

    def test_edge_case3(self):
        self.assertEqual(substract_elements((), (1, 2, 3)), ((1, 2, 3),))

    def test_edge_case4(self):
        self.assertEqual(substract_elements((1, 2, 3), (4, 5)), ((-3, -3),))

    def test_edge_case5(self):
        self.assertEqual(substract_elements((1, 2), (3, 4, 5)), ((-2, -2),))

    def test_edge_case6(self):
        self.assertEqual(substract_elements((1, 2, 3, 4), (5, 6, 7)), ((-4, -4, -4),))
