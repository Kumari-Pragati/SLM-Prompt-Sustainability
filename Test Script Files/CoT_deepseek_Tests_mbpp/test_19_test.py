import unittest
from mbpp_19_code import test_duplicate

class TestDuplicate(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(test_duplicate([1, 2, 3, 4, 5]))

    def test_duplicate_case(self):
        self.assertTrue(test_duplicate([1, 2, 2, 3, 4]))

    def test_empty_list(self):
        self.assertFalse(test_duplicate([]))

    def test_single_element(self):
        self.assertFalse(test_duplicate([1]))

    def test_duplicate_elements(self):
        self.assertTrue(test_duplicate([1, 1, 1, 1]))

    def test_negative_numbers(self):
        self.assertTrue(test_duplicate([-1, -2, -2, -3]))

    def test_mixed_numbers(self):
        self.assertTrue(test_duplicate([1, -2, 3, -4]))

    def test_zero(self):
        self.assertTrue(test_duplicate([0, 0]))

    def test_large_numbers(self):
        self.assertTrue(test_duplicate([1000000, 2000000, 2000000]))

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            test_duplicate([1, '2', 3, 4])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            test_duplicate(123456)
