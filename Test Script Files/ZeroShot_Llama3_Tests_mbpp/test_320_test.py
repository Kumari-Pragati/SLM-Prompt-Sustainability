import unittest
from mbpp_320_code import sum_difference

class TestSumDifference(unittest.TestCase):

    def test_sum_difference(self):
        self.assertEqual(sum_difference(1), 0)
        self.assertEqual(sum_difference(2), 2)
        self.assertEqual(sum_difference(3), 2)
        self.assertEqual(sum_difference(4), 0)
        self.assertEqual(sum_difference(5), -15)
        self.assertEqual(sum_difference(10), -264)
        self.assertEqual(sum_difference(20), -406)

    def test_sum_difference_edge_cases(self):
        self.assertEqual(sum_difference(0), 0)
        self.assertEqual(sum_difference(-1), None)

    def test_sum_difference_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_difference("a")
        with self.assertRaises(TypeError):
            sum_difference(None)
