import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):
    def test_same_length(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 3], [3, 2, 1]), 3)
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 4], [3, 2, 1]), 0)

    def test_different_length(self):
        self.assertEqual(count_samepair([1, 2, 3], [2, 1], [3]), 1)
        self.assertEqual(count_samepair([1, 2, 3], [2, 1, 4], [3, 2, 1, 5]), 1)

    def test_empty_lists(self):
        self.assertEqual(count_samepair([], [], []), 0)
        self.assertEqual(count_samepair([1], [], [1]), 1)
        self.assertEqual(count_samepair([], [1], []), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_samepair, 1, 2, 3)
        self.assertRaises(TypeError, count_samepair, [1], '2', [3])
        self.assertRaises(TypeError, count_samepair, [1], [2], '3')
