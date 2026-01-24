import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(answer(2, 5), (2, 4))
        self.assertEqual(answer(3, 7), (3, 6))

    def test_edge_cases(self):
        self.assertEqual(answer(2, 2), (-1))
        self.assertEqual(answer(5, 10), (5, 10))

    def test_boundary_cases(self):
        self.assertEqual(answer(1, 2), (-1))
        self.assertEqual(answer(2, 4), (2, 4))
        self.assertEqual(answer(4, 8), (2, 4))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            answer('a', 5)
        with self.assertRaises(TypeError):
            answer(2, 'b')
