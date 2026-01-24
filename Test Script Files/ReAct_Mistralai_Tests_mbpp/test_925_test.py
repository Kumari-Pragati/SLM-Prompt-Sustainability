import unittest
from mbpp_925_code import mutiple_tuple

class TestMultipleTuple(unittest.TestCase):

    def test_empty_list(self):
        """Test if function returns 1 for empty list"""
        self.assertEqual(mutiple_tuple([]), 1)

    def test_single_element(self):
        """Test if function returns the same number for a single element list"""
        for num in range(10):
            self.assertEqual(mutiple_tuple([num]), num)

    def test_positive_numbers(self):
        """Test if function correctly multiplies positive numbers"""
        for num1 in range(1, 100):
            for num2 in range(1, 100):
                self.assertEqual(mutiple_tuple([num1, num2]), num1 * num2)

    def test_negative_numbers(self):
        """Test if function correctly multiplies negative numbers"""
        for num1 in range(-10, 0):
            for num2 in range(-10, 0):
                self.assertEqual(mutiple_tuple([num1, num2]), num1 * num2)

    def test_zero(self):
        """Test if function correctly handles zero"""
        self.assertEqual(mutiple_tuple([0]), 0)
        self.assertEqual(mutiple_tuple([0, 1]), 0)
        self.assertEqual(mutiple_tuple([1, 0]), 0)

    def test_mixed_numbers(self):
        """Test if function correctly handles a mix of positive and negative numbers"""
        for num1 in range(-10, 10):
            for num2 in range(-10, 10):
                if num1 == 0 or num2 == 0:
                    continue
                self.assertNotEqual(mutiple_tuple([num1, num2]), 0)
