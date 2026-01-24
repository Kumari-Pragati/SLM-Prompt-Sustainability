import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, K)], K))
        self.assertTrue(check_k_elements([(K,), (1, 2, 3)], K))
        self.assertTrue(check_k_elements([(K, K, K)], K))

    def test_edge_cases(self):
        self.assertFalse(check_k_elements([(1, 2, 3)], K))
        self.assertFalse(check_k_elements([], K))
        self.assertFalse(check_k_elements([(K, 1, 2)], K))
        self.assertFalse(check_k_elements([(1, K, 2)], K))
        self.assertFalse(check_k_elements([(1, 2, K)], K))

    def test_boundary_cases(self):
        self.assertTrue(check_k_elements([(K-1, K, K+1)], K))
        self.assertTrue(check_k_elements([(K-1, K, K+1), (K-2, K, K+2)], K))

    def test_invalid_input(self):
        self.assertRaises(TypeError, check_k_elements, 'test_list', K)
        self.assertRaises(TypeError, check_k_elements, [1], K)
        self.assertRaises(TypeError, check_k_elements, [(1,), K],)
        self.assertRaises(TypeError, check_k_elements, [(1, 2), K],)
        self.assertRaises(TypeError, check_k_elements, [(1, 2, 3), ], K)
