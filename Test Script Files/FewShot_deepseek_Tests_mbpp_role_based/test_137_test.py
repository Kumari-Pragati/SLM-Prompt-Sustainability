import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):
    def test_typical_case(self):
        nums = array('i', [0, 1, 0, 2, 0, 3])
        self.assertEqual(zero_count(nums), 0.5)

    def test_all_zeros(self):
        nums = array('i', [0, 0, 0, 0, 0])
        self.assertEqual(zero_count(nums), 1.0)

    def test_all_non_zeros(self):
        nums = array('i', [1, 2, 3, 4, 5])
        self.assertEqual(zero_count(nums), 0.0)

    def test_empty_array(self):
        nums = array('i', [])
        self.assertEqual(zero_count(nums), 0.0)

    def test_single_zero(self):
        nums = array('i', [0])
        self.assertEqual(zero_count(nums), 1.0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            zero_count("not an array")
