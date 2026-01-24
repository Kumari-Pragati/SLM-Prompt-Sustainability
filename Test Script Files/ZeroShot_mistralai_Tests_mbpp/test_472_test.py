import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(check_Consecutive([]))

    def test_single_element_list(self):
        for element in range(-100, 101):
            self.assertTrue(check_Consecutive([element]))

    def test_consecutive_list(self):
        for start in range(-100, 101):
            for end in range(start + 1, min(start + 10, 101)):
                self.assertTrue(check_Consecutive(list(range(start, end + 1))))

    def test_non_consecutive_list(self):
        for start in range(-100, 101):
            for end in range(start + 3, min(start + 10, 101)):
                self.assertFalse(check_Consecutive(list(range(start, end + 1))))
