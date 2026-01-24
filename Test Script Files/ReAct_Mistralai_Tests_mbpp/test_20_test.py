import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_even_numbers(self):
        for num in range(2, 100, 2):
            self.assertFalse(is_woodall(num))

    def test_odd_numbers(self):
        for num in range(1, 100):
            if num == 1:
                self.assertTrue(is_woodall(num))
            elif num == 2:
                self.assertTrue(is_woodall(num))
            else:
                self.assertTrue(is_woodall(num)) if is_woodall(num) else self.assertFalse(is_woodall(num))

    def test_edge_cases(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(-1))
        self.assertFalse(is_woodall(1000000))
