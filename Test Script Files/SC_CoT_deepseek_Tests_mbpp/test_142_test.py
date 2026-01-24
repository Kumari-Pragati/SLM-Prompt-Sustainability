import unittest
from mbpp_142_code import count_samepair

class TestCountSamePair(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_edge_case(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [1], [1]), 1)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_corner_case(self):
        self.assertEqual(count_samepair([1, 2, 3], [3, 2, 1], [1, 2, 3]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 4]), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], [1, 2, 3], 1)
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], 1, [1, 2, 3])
        with self.assertRaises(TypeError):
            count_samepair(1, [1, 2, 3], [1, 2, 3])
