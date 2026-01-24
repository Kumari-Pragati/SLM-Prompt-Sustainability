import unittest
from mbpp_256_code import count_Primes_nums

class TestCountPrimesNums(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Primes_nums(10), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_Primes_nums(0), 0)
        self.assertEqual(count_Primes_nums(1), 0)
        self.assertEqual(count_Primes_nums(2), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_Primes_nums(3), 2)
        self.assertEqual(count_Primes_nums(100), 25)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Primes_nums('10')
        with self.assertRaises(TypeError):
            count_Primes_nums(None)
