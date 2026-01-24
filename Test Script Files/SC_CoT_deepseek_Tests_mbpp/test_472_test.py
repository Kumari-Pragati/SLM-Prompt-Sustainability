import unittest

from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_single_element(self):
        self.assertTrue(check_Consecutive([1]))

    def test_empty_list(self):
        self.assertTrue(check_Consecutive([]))

    def test_non_consecutive_elements(self):
        self.assertFalse(check_Consecutive([1, 3, 2, 4, 5]))

    def test_duplicate_elements(self):
        self.assertFalse(check_Consecutive([1, 2, 2, 4, 5]))

    def test_negative_numbers(self):
        self.assertTrue(check_Consecutive([-1, 0, 1, 2, 3]))

    def test_large_numbers(self):
        self.assertTrue(check_Consecutive(list(range(100000, 100005))))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Consecutive("1, 2, 3, 4, 5")

        with self.assertRaises(TypeError):
            check_Consecutive([1, "2", 3, 4, 5])

        with self.assertRaises(TypeError):
            check_Consecutive([1, 2, None, 4, 5])

        with self.assertRaises(TypeError):
            check_Consecutive([1, 2, 3, 4, float('nan')])
