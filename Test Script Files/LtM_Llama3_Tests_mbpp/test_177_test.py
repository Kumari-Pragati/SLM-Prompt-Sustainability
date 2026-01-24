import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(2, 4), (2, 4))
        self.assertEqual(answer(3, 6), (3, 6))

    def test_edge(self):
        self.assertEqual(answer(0, 1), (0, 1))
        self.assertEqual(answer(1, 1), (-1))
        self.assertEqual(answer(2, 0), (-1))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            answer('a', 2)
        with self.assertRaises(TypeError):
            answer(1, 'b')
