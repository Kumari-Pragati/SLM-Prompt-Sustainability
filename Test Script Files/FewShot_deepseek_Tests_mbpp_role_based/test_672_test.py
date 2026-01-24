import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_of_three(10, 20, 15), 20)

    def test_boundary_conditions(self):
        self.assertEqual(max_of_three(-100, -200, -300), -100)
        self.assertEqual(max_of_three(0, 0, 0), 0)
        self.assertEqual(max_of_three(1000000000, 1000000000, 1000000000), 1000000000)

    def test_edge_conditions(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(3, 2, 1), 3)
        self.assertEqual(max_of_three(2, 3, 1), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            max_of_three("10", 20, 15)
        with self.assertRaises(TypeError):
            max_of_three(10, "20", 15)
        with self.assertRaises(TypeError):
            max_of_three(10, 20, "15")
