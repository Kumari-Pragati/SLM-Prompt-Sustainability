import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(5, 5, 5), 5)
        self.assertEqual(max_of_three(-1, -2, -3), -1)

    def test_edge_cases(self):
        self.assertEqual(max_of_three(1, 1, 1), 1)
        self.assertEqual(max_of_three(-1, -1, -1), -1)
        self.assertEqual(max_of_three(0, 0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_three('a', 'b', 'c')
        with self.assertRaises(TypeError):
            max_of_three(1, 'b', 3)
        with self.assertRaises(TypeError):
            max_of_three(1, 2, 'c')
