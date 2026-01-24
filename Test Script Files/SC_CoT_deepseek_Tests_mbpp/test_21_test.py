import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiples_of_num(5, 10), [10, 20, 30, 40, 50])

    def test_boundary_case(self):
        self.assertEqual(multiples_of_num(1, 1), [1])

    def test_edge_case(self):
        self.assertEqual(multiples_of_num(0, 10), [])
        self.assertEqual(multiples_of_num(5, 0), [])

    def test_special_case(self):
        self.assertEqual(multiples_of_num(3, 15), [15, 30, 45])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            multiples_of_num("5", 10)
        with self.assertRaises(TypeError):
            multiples_of_num(5, "10")
        with self.assertRaises(TypeError):
            multiples_of_num("5", "10")
