import unittest
from mbpp_26_code import check_k_elements

class TestCheckKElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(check_k_elements([], 1))

    def test_single_element_list(self):
        for k in range(1, 6):
            self.assertTrue(check_k_elements([k], k))
            self.assertFalse(check_k_elements([k], 1))

    def test_list_with_k_and_non_k(self):
        for k in range(1, 6):
            self.assertFalse(check_k_elements([k, k, 1], k))
            self.assertTrue(check_k_elements([k, k, k], k))

    def test_list_with_only_non_k(self):
        for k in range(1, 6):
            self.assertFalse(check_k_elements([1, 2, 3], k))

    def test_list_with_duplicates(self):
        for k in range(1, 6):
            self.assertTrue(check_k_elements([k, k, k], k))

    def test_list_with_negative_numbers(self):
        for k in range(1, 6):
            self.assertRaises(TypeError, check_k_elements, [[-1, -2, -3], k])

    def test_list_with_non_integer_elements(self):
        for k in range(1, 6):
            self.assertRaises(TypeError, check_k_elements, [['a', 'b', 'c'], k])
