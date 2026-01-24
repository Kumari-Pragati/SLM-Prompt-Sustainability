import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(5, 2, 1), 5)
        self.assertEqual(max_of_three(10, 10, 10), 10)

    def test_edge_cases(self):
        self.assertEqual(max_of_three(1, 1, 1), 1)
        self.assertEqual(max_of_three(-1, -2, -3), -1)
        self.assertEqual(max_of_three(0, 0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(max_of_three(1, 2, 1), 2)
        self.assertEqual(max_of_three(3, 2, 1), 3)
        self.assertEqual(max_of_three(1, 1, 2), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_three('a', 2, 3)
        with self.assertRaises(TypeError):
            max_of_three(1, 'b', 3)
        with self.assertRaises(TypeError):
            max_of_three(1, 2, 'c')
