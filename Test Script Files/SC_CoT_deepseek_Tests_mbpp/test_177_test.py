import unittest

from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(answer(2, 8), (2, 4))

    def test_boundary_case(self):
        self.assertEqual(answer(1, 2), (1, 2))

    def test_edge_case(self):
        self.assertEqual(answer(0, 0), (0, 0))
        self.assertEqual(answer(1, 1), (1, 2))
        self.assertEqual(answer(2, 3), (-1,))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            answer("2", 4)
        with self.assertRaises(TypeError):
            answer(2, "4")
