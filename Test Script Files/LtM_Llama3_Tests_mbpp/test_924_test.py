import unittest
from mbpp_924_code import max_of_two

class TestMaxOfTwo(unittest.TestCase):
    def test_simple_positive(self):
        self.assertEqual(max_of_two(5, 3), 5)

    def test_simple_negative(self):
        self.assertEqual(max_of_two(-5, -3), -5)

    def test_edge_equal(self):
        self.assertEqual(max_of_two(5, 5), 5)

    def test_edge_reverse(self):
        self.assertEqual(max_of_two(3, 5), 5)

    def test_edge_reverse_negative(self):
        self.assertEqual(max_of_two(-5, -3), -3)

    def test_edge_reverse_positive(self):
        self.assertEqual(max_of_two(5, 3), 5)

    def test_edge_reverse_zero(self):
        self.assertEqual(max_of_two(0, 0), 0)

    def test_edge_reverse_zero_negative(self):
        self.assertEqual(max_of_two(0, -5), 0)

    def test_edge_reverse_zero_positive(self):
        self.assertEqual(max_of_two(5, 0), 5)

    def test_edge_reverse_zero_negative_reverse(self):
        self.assertEqual(max_of_two(-5, 0), -5)

    def test_edge_reverse_zero_positive_reverse(self):
        self.assertEqual(max_of_two(0, 5), 5)
