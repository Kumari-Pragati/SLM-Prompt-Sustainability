import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(count_tuplex([(1, 2), (2, 3), (1, 2)], 1), 2)
        self.assertEqual(count_tuplex([(1, 2), (2, 3), (1, 2)], 2), 1)
        self.assertEqual(count_tuplex([], 1), 0)
        self.assertEqual(count_tuplex([(1, 2), (2, 3)], 1), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_tuplex([(1, 2)], 1), 1)
        self.assertEqual(count_tuplex([(1, 2), (1, 2)], 1), 2)
        self.assertEqual(count_tuplex([(1, 2), (2, 3)], 4), 0)
        self.assertEqual(count_tuplex([(1, 2), (2, 3)], 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_tuplex('not a tuple', 1)
        with self.assertRaises(TypeError):
            count_tuplex([1], 1.5)
