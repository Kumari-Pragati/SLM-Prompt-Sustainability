import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):

    def test_round_and_sum(self):
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0]), 6.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0]), 10.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0, 5.0]), 15.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), 21.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]), 28.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]), 36.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]), 45.0)
        self.assertEqual(round_and_sum([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]), 55.0)

    def test_round_and_sum_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, 2, 3, 'a', 5, 6, 7, 8, 9, 10])

    def test_round_and_sum_with_non_list(self):
        with self.assertRaises(TypeError):
            round_and_sum(1)
