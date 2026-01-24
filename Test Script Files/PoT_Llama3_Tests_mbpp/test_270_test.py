import unittest
from mbpp_270_code import sum_even_and_even_index

class TestSumEvenAndEvenIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 6), 12)

    def test_edge_case(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 3), 2)

    def test_edge_case2(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 1), 2)

    def test_edge_case3(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 0), 0)

    def test_edge_case4(self):
        self.assertEqual(sum_even_and_even_index([1, 2, 3, 4, 5, 6], 7), 12)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_even_and_even_index('hello', 5)
