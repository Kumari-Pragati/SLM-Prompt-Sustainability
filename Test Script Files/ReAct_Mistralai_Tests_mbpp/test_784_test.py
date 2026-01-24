import unittest
from mbpp_784_code import mul_even_odd

class TestMulEvenOdd(unittest.TestCase):

    def test_empty_list(self):
        """Test mul_even_odd with an empty list"""
        with self.assertRaises(StopIteration):
            mul_even_odd([])

    def test_single_even_or_odd(self):
        """Test mul_even_odd with a list containing only one even or odd number"""
        for num in [2, 3, 5, 7]:
            with self.subTest(num=num):
                self.assertEqual(mul_even_odd([num]), -1)

    def test_single_even_and_odd(self):
        """Test mul_even_odd with a list containing one even and one odd number"""
        for even, odd in [(2, 3), (3, 2), (5, 7), (7, 5)]:
            with self.subTest(even=even, odd=odd):
                self.assertEqual(mul_even_odd([even, odd]), even * odd)

    def test_multiple_even_and_odd(self):
        """Test mul_even_odd with a list containing multiple even and odd numbers"""
        for even_list, odd_list in [((2, 4, 6), (1, 3, 5)), ((2, 4, 6), (1, 3)),
                                    ((2, 4, 6), (1, 3, 5, 7)), ((2, 4), (1, 3, 5))]:
            with self.subTest(even_list=even_list, odd_list=odd_list):
                self.assertEqual(mul_even_odd(even_list + odd_list),
                                 mul_even_odd(even_list) * mul_even_odd(odd_list))

    def test_mixed_even_and_odd_with_duplicates(self):
        """Test mul_even_odd with a list containing multiple even and odd numbers with duplicates"""
        for even_list, odd_list in [((2, 2, 4, 6), (1, 1, 3, 5)), ((2, 4, 6), (1, 3, 1, 5)),
                                    ((2, 4, 6, 2), (1, 3, 5, 1))]:
            with self.subTest(even_list=even_list, odd_list=odd_list):
                self.assertEqual(mul_even_odd(even_list + odd_list),
                                 mul_even_odd(even_list) * mul_even_odd(odd_list))

    def test_list_with_only_even_numbers(self):
        """Test mul_even_odd with a list containing only even numbers"""
        for even_list in [(2, 4, 6, 8), (2, 4, 6), (2, 4, 6, 8, 2)]:
            with self.subTest(even_list=even_list):
                self.assertEqual(mul_even_odd(even_list), -1)

    def test_list_with_only_odd_numbers(self):
        """Test mul_even_odd with a list containing only odd numbers"""
        for odd_list in [(1, 3, 5, 7), (1, 3, 5), (1, 3, 5, 7, 1)]:
            with self.subTest(odd_list=odd_list):
                self.assertEqual(mul_even_odd(odd_list), -1)
