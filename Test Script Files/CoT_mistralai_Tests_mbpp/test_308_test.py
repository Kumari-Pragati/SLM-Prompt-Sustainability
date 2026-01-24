import unittest
from mbpp_308_code import large_product

class TestLargeProduct(unittest.TestCase):

    def test_empty_lists(self):
        self.assertListEqual(large_product([], [], 0), [])
        self.assertListEqual(large_product([], [1, 2, 3], 3), [1*2, 1*3, 2*3])
        self.assertListEqual(large_product([1, 2, 3], [], 3), [1*2, 1*3, 2*3])

    def test_single_element_lists(self):
        self.assertListEqual(large_product([1], [2], 1), [1*2])
        self.assertListEqual(large_product([2], [1], 1), [1*2])

    def test_simple_lists(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 6), [12*6, 1*6, 2*6, 1*5, 2*5, 3*5, 1*4, 2*4, 3*4])
        self.assertListEqual(large_product([1, 2, 3], [6, 5, 4], 6), [18, 12, 6, 15, 10, 9])
        self.assertListEqual(large_product([6, 5, 4], [1, 2, 3], 6), [18, 12, 6, 15, 10, 9])

    def test_boundary_conditions(self):
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 1), [12])
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 7), [12, 1*6, 2*6, 1*5, 2*5, 3*5, 1*4])
        self.assertListEqual(large_product([1, 2, 3], [4, 5, 6], 0), [])

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, large_product, [1, 2, 3], [4, 5, 6], 'N')
        self.assertRaises(TypeError, large_product, [1, 2, 3], [4, 5, 6], -1)
