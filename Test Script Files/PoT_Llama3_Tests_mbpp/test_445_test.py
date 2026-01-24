import unittest
from mbpp_445_code import index_multiplication

class TestIndexMultiplication(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6)), ((1*4, 1*5, 1*6), (2*4, 2*5, 2*6), (3*4, 3*5, 3*6)))

    def test_edge_case(self):
        self.assertEqual(index_multiplication((1, 2), (3, 4)), ((1*3, 1*4), (2*3, 2*4)))

    def test_edge_case2(self):
        self.assertEqual(index_multiplication((1, 2, 3), ()), (),)

    def test_edge_case3(self):
        self.assertEqual(index_multiplication((), (1, 2, 3)), (),)

    def test_edge_case4(self):
        self.assertEqual(index_multiplication((1, 2), (1, 2)), ((1*1, 1*2), (2*1, 2*2)))

    def test_edge_case5(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5)), ((1*4, 1*5), (2*4, 2*5), (3*4, 3*5)))

    def test_edge_case6(self):
        self.assertEqual(index_multiplication((1, 2), (3, 4, 5)), ((1*3, 1*4, 1*5), (2*3, 2*4, 2*5)))

    def test_edge_case7(self):
        self.assertEqual(index_multiplication((1, 2, 3, 4), (5, 6)), ((1*5, 1*6), (2*5, 2*6), (3*5, 3*6), (4*5, 4*6)))

    def test_edge_case8(self):
        self.assertEqual(index_multiplication((1, 2, 3), (4, 5, 6, 7)), ((1*4, 1*5, 1*6, 1*7), (2*4, 2*5, 2*6, 2*7), (3*4, 3*5, 3*6, 3*7))
