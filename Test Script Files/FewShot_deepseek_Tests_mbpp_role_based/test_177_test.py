import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(answer(1, 2), (1, 2))

    def test_boundary_condition(self):
        self.assertEqual(answer(0, 0), (0, 0))

    def test_edge_condition(self):
        self.assertEqual(answer(1, 1), (1, 2))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            answer("1", 2)
