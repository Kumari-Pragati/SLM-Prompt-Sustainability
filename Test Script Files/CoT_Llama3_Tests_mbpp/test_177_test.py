import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(answer(1, 3), (1, 2))
        self.assertEqual(answer(2, 5), (2, 4))
        self.assertEqual(answer(3, 7), (3, 6))

    def test_edge_cases(self):
        self.assertEqual(answer(0, 1), (0, 0))
        self.assertEqual(answer(1, 1), (-1))
        self.assertEqual(answer(2, 2), (-1))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            answer('a', 3)
        with self.assertRaises(TypeError):
            answer(1, 'b')
        with self.assertRaises(TypeError):
            answer(None, None)
