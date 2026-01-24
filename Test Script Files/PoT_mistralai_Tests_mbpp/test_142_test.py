import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_samepair([1, 2, 3, 1, 2], [1, 2, 3, 1, 2], [1, 2, 3, 1, 2]), 4)

    def test_edge_case_1(self):
        self.assertEqual(count_samepair([], [], []), 0)

    def test_edge_case_2(self):
        self.assertEqual(count_samepair([1], [1], []), 0)

    def test_edge_case_3(self):
        self.assertEqual(count_samepair([1, 2], [1, 2], []), 0)

    def test_edge_case_4(self):
        self.assertEqual(count_samepair([1, 2], [1, 3], []), 0)

    def test_corner_case_1(self):
        self.assertEqual(count_samepair([1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 1, 2]), 2)

    def test_corner_case_2(self):
        self.assertEqual(count_samepair([1, 1, 2, 2], [1, 2, 1, 3], [1, 2, 1, 2]), 1)
