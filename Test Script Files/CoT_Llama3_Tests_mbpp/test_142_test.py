import unittest
from mbpp_142_code import count_samepair

class TestCountSamepair(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 3]), 3)

    def test_edge1(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 4]), 2)

    def test_edge2(self):
        self.assertEqual(count_samepair([1, 1, 1], [1, 1, 1], [1, 1, 1]), 3)

    def test_edge3(self):
        self.assertEqual(count_samepair([1, 2, 3], [1, 2, 3], []), 0)

    def test_edge4(self):
        self.assertEqual(count_samepair([], [1, 2, 3], [1, 2, 3]), 0)

    def test_edge5(self):
        self.assertEqual(count_samepair([1, 2, 3], [], [1, 2, 3]), 0)

    def test_invalid1(self):
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], 'a', [1, 2, 3])

    def test_invalid2(self):
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], [1, 2, 3], 'a')

    def test_invalid3(self):
        with self.assertRaises(TypeError):
            count_samepair('a', [1, 2, 3], [1, 2, 3])

    def test_invalid4(self):
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], [1, 2, 3], [1, 2, 'a'])

    def test_invalid5(self):
        with self.assertRaises(TypeError):
            count_samepair([1, 2, 3], [1, 2, 3.5], [1, 2, 3])
