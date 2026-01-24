import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_max_of_three_typical(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)

    def test_max_of_three_edge1(self):
        self.assertEqual(max_of_three(1, 1, 1), 1)

    def test_max_of_three_edge2(self):
        self.assertEqual(max_of_three(-1, -2, -3), -1)

    def test_max_of_three_edge3(self):
        self.assertEqual(max_of_three(0, 0, 0), 0)

    def test_max_of_three_invalid_input1(self):
        with self.assertRaises(TypeError):
            max_of_three('a', 2, 3)

    def test_max_of_three_invalid_input2(self):
        with self.assertRaises(TypeError):
            max_of_three(1, 'b', 3)

    def test_max_of_three_invalid_input3(self):
        with self.assertRaises(TypeError):
            max_of_three(1, 2, 'c')
