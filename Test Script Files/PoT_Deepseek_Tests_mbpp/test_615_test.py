import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(average_tuple([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [4.0, 5.0, 6.0])

    def test_empty_list(self):
        self.assertEqual(average_tuple([]), [])

    def test_single_number(self):
        self.assertEqual(average_tuple([[1]]), [1])

    def test_different_length_lists(self):
        self.assertAlmostEqual(average_tuple([[1, 2], [3, 4, 5]]), [1.5, 4.0])

    def test_negative_numbers(self):
        self.assertAlmostEqual(average_tuple([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), [-4.0, -5.0, -6.0])

    def test_zeroes(self):
        self.assertAlmostEqual(average_tuple([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [0, 0, 0])

    def test_large_numbers(self):
        self.assertAlmostEqual(average_tuple([[1000, 2000, 3000], [4000, 5000, 6000], [7000, 8000, 9000]]), [4000.0, 5000.0, 6000.0])
