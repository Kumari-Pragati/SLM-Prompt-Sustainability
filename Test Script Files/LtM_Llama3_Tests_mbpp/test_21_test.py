import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(multiples_of_num(2, 10), [2, 4, 6, 8, 10])
        self.assertEqual(multiples_of_num(3, 15), [3, 6, 9, 12, 15])
        self.assertEqual(multiples_of_num(5, 25), [5, 10, 15, 20, 25])

    def test_edge_cases(self):
        self.assertEqual(multiples_of_num(1, 1), [])
        self.assertEqual(multiples_of_num(1, 2), [1])
        self.assertEqual(multiples_of_num(2, 1), [])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            multiples_of_num('a', 10)
        with self.assertRaises(TypeError):
            multiples_of_num(2, 'a')
