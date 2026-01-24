import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(multiples_of_num(2, 10), [0, 2, 4, 6, 8, 10])

    def test_edge_cases(self):
        self.assertEqual(multiples_of_num(1, 1), [])
        self.assertEqual(multiples_of_num(1, 0), [])

    def test_boundary_cases(self):
        self.assertEqual(multiples_of_num(1, 5), [0, 1, 2, 3, 4])
        self.assertEqual(multiples_of_num(2, 5), [0, 2, 4])

    def test_special_cases(self):
        self.assertEqual(multiples_of_num(3, 10), [0, 3, 6, 9])
        self.assertEqual(multiples_of_num(4, 10), [0, 4, 8])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            multiples_of_num('a', 10)
        with self.assertRaises(TypeError):
            multiples_of_num(2, 'a')
