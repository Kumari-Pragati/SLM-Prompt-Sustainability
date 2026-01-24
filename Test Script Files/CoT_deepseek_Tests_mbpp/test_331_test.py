import unittest
from mbpp_331_code import count_unset_bits

class TestCountUnsetBits(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_unset_bits(0), 0)
        self.assertEqual(count_unset_bits(1), 1)
        self.assertEqual(count_unset_bits(2), 1)
        self.assertEqual(count_unset_bits(3), 0)
        self.assertEqual(count_unset_bits(4), 1)
        self.assertEqual(count_unset_bits(5), 0)
        self.assertEqual(count_unset_bits(6), 2)
        self.assertEqual(count_unset_bits(7), 0)
        self.assertEqual(count_unset_bits(8), 1)

    def test_edge_cases(self):
        self.assertEqual(count_unset_bits(9), 0)
        self.assertEqual(count_unset_bits(10), 2)
        self.assertEqual(count_unset_bits(11), 1)
        self.assertEqual(count_unset_bits(12), 2)
        self.assertEqual(count_unset_bits(13), 1)
        self.assertEqual(count_unset_bits(14), 2)
        self.assertEqual(count_unset_bits(15), 0)
        self.assertEqual(count_unset_bits(16), 1)

    def test_boundary_conditions(self):
        self.assertEqual(count_unset_bits(17), 0)
        self.assertEqual(count_unset_bits(18), 1)
        self.assertEqual(count_unset_bits(19), 0)
        self.assertEqual(count_unset_bits(20), 2)
        self.assertEqual(count_unset_bits(21), 1)
        self.assertEqual(count_unset_bits(22), 2)
        self.assertEqual(count_unset_bits(23), 1)
        self.assertEqual(count_unset_bits(24), 2)
        self.assertEqual(count_unset_bits(25), 1)
        self.assertEqual(count_unset_bits(26), 2)
        self.assertEqual(count_unset_bits(27), 0)
        self.assertEqual(count_unset_bits(28), 1)
        self.assertEqual(count_unset_bits(29), 0)
        self.assertEqual(count_unset_bits(30), 2)
        self.assertEqual(count_unset_bits(31), 0)
        self.assertEqual(count_unset_bits(32), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_unset_bits("invalid")
        with self.assertRaises(ValueError):
            count_unset_bits(-1)
