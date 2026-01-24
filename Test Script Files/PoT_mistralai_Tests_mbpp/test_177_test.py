import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(2, 4), (2, 4))
        self.assertEqual(answer(3, 6), (3, 6))

    def test_edge_case(self):
        self.assertEqual(answer(0, 1), (-1,))
        self.assertEqual(answer(1, 0), (-1,))
        self.assertEqual(answer(1, -1), (-1,))

    def test_boundary_case(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(2, 2), (2, 4))
        self.assertEqual(answer(3, 2), (3, 6))
        self.assertEqual(answer(4, 2), (-1,))
