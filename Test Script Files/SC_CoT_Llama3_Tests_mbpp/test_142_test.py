import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_edge_cases(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 1, 1]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3, 4]), 3)
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [1], []), 0)

    def test_corner_cases(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 4]), 2)
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 1, 2]), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_samepair(1, 2, 3)
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], 'abc', [1, 2, 3])
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], [1, 2, 3], 'abc')
