import unittest
from mbpp_838_code import min_Swaps

class TestMinSwaps(unittest.TestCase):

    def test_empty_strings(self):
        self.assertEqual(min_Swaps('', ''), 0)
        self.assertEqual(min_Swaps('', '1'), -1)
        self.assertEqual(min_Swaps('1', ''), -1)

    def test_single_element_strings(self):
        self.assertEqual(min_Swaps('0', '1'), 1)
        self.assertEqual(min_Swaps('1', '0'), 1)
        self.assertEqual(min_Swaps('0', '0'), 0)
        self.assertEqual(min_Swaps('1', '1'), 0)

    def test_identical_strings(self):
        self.assertEqual(min_Swaps('000', '000'), 0)
        self.assertEqual(min_Swaps('111', '111'), 0)

    def test_alternating_strings(self):
        self.assertEqual(min_Swaps('010101', '101010'), 2)
        self.assertEqual(min_Swaps('101010', '010101'), 2)

    def test_long_strings(self):
        self.assertEqual(min_Swaps('00000000000000000000000000000000', '11111111111111111111111111111111'), 50)
        self.assertEqual(min_Swaps('11111111111111111111111111111111', '00000000000000000000000000000000'), 50)

    def test_error_cases(self):
        self.assertEqual(min_Swaps('0', '0'), -1)
        self.assertEqual(min_Swaps('1', '1'), -1)
        self.assertEqual(min_Swaps('01', '10'), -1)
        self.assertEqual(min_Swaps('01', '1'), -1)
        self.assertEqual(min_Swaps('01', '2'), -1)
