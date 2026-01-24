import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6)], 7))
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 7)], 7))

    def test_edge_conditions(self):
        self.assertTrue(check_k_elements([], 0))
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6)], 7))
        self.assertTrue(check_k_elements([(7, 7, 7), (7, 7, 7)], 7))

    def test_complex_cases(self):
        self.assertFalse(check_k_elements([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 10))
        self.assertTrue(check_k_elements([(1, 2, 3), (4, 5, 6), (6, 6, 6)], 6))
