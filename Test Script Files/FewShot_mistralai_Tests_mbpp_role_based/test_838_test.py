import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    def test_same_strings(self):
        self.assertEqual(min_Swaps('000', '000'), 0)

    def test_identical_strings(self):
        self.assertEqual(min_Swaps('111', '111'), 0)

    def test_complementary_strings(self):
        self.assertEqual(min_Swaps('010', '101'), 2)

    def test_longer_string(self):
        self.assertEqual(min_Swaps('0001', '1000'), 1)

    def test_shorter_string(self):
        self.assertEqual(min_Swaps('000', '0001'), 1)

    def test_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)

    def test_invalid_input_1(self):
        with self.assertRaises(ValueError):
            min_Swaps('01', '1')

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            min_Swaps('010', '10')
