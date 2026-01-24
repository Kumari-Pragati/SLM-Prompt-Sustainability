import unittest
from mbpp_177_code import answer

class TestAnswerFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(answer(3, 6), (3, 6))

    def test_boundary_case(self):
        self.assertEqual(answer(1, 2), (1, 2))

    def test_edge_case(self):
        self.assertEqual(answer(0, 0), (0, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            answer("a", 1)
        with self.assertRaises(TypeError):
            answer(1, "b")

    def test_error_behavior(self):
        self.assertEqual(answer(3, 2), -1)
