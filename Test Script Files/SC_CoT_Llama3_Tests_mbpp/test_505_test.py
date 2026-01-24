import unittest
from mbpp_505_code import re_order

class TestReOrder(unittest.TestCase):

    def test_typical_input(self):
        A = [1, 2, 3, 0, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [1, 2, 3, 0, 0, 0])

    def test_edge_case(self):
        A = [1, 0, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [1, 0, 0, 0])

    def test_edge_case2(self):
        A = [0, 0, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [0, 0, 0, 0])

    def test_edge_case3(self):
        A = [1, 1, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [1, 1, 0, 0])

    def test_edge_case4(self):
        A = [0, 1, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [0, 1, 0, 0])

    def test_edge_case5(self):
        A = [1, 1, 1, 0, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [1, 1, 1, 0, 0, 0])

    def test_edge_case6(self):
        A = [0, 0, 0, 1, 0, 0]
        result = re_order(A)
        self.assertEqual(result, [0, 0, 0, 1, 0, 0])

    def test_edge_case7(self):
        A = [0, 0, 0, 0, 1, 0]
        result = re_order(A)
        self.assertEqual(result, [0, 0, 0, 0, 1, 0])

    def test_edge_case8(self):
        A = [0, 0, 0, 0, 0, 1]
        result = re_order(A)
        self.assertEqual(result, [0, 0, 0, 0, 0, 1])

    def test_invalid_input(self):
        A = None
        with self.assertRaises(TypeError):
            re_order(A)

    def test_invalid_input2(self):
        A = "string"
        with self.assertRaises(TypeError):
            re_order(A)
