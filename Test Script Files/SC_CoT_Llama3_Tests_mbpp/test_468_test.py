import unittest
from mbpp_468_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_typical_input(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 20)

    def test_edge_case(self):
        arr = [5, 4, 3, 2, 1]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 20)

    def test_edge_case2(self):
        arr = [1, 2, 3, 4, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 20)

    def test_edge_case3(self):
        arr = [5, 5, 5, 5, 5]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 3125)

    def test_edge_case4(self):
        arr = [1, 1, 1, 1, 1]
        n = len(arr)
        self.assertEqual(max_product(arr, n), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_product('string', 5)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            max_product([1, 2, 3],'string')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            max_product([], None)
