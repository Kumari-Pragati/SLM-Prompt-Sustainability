import unittest
from mbpp_339_code import find_Divisor

class TestFindDivisor(unittest.TestCase):

    def test_find_divisor_normal(self):
        self.assertEqual(find_Divisor(6, 3), 3)
        self.assertEqual(find_Divisor(10, 2), 2)
        self.assertEqual(find_Divisor(18, 6), 6)

    def test_find_divisor_edge_cases(self):
        self.assertEqual(find_Divisor(0, 1), 2)
        self.assertEqual(find_Divisor(1, 0), 2)
        self.assertEqual(find_Divisor(1, 1), 1)

    def test_find_divisor_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Divisor('a', 'b')
        with self.assertRaises(TypeError):
            find_Divisor([1, 2, 3], 4)
