import unittest
from mbpp_177_code import answer

class TestAnswer(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(answer(1, 2), (1, 2))
        self.assertEqual(answer(2, 4), (2, 4))
        self.assertEqual(answer(3, 6), (3, 6))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(answer(0, 1), -1)
        self.assertEqual(answer(1, 0), -1)
        self.assertEqual(answer(2147483647, 4294967295), -1)
        self.assertEqual(answer(4294967295, 2147483647), -1)

    def test_complex_scenarios(self):
        self.assertEqual(answer(1000000, 2000000), (1000000, 2000000))
        self.assertEqual(answer(2000000, 4000000), (2000000, 4000000))
        self.assertEqual(answer(4000000, 8000000), (4000000, 8000000))
