import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_max_of_three(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(10, 2, 1), 10)
        self.assertEqual(max_of_three(-1, -2, -3), -1)
        self.assertEqual(max_of_three(0, 0, 0), 0)
        self.assertEqual(max_of_three(-1, 0, -2), -1)
        self.assertEqual(max_of_three(1, 1, 1), 1)
        self.assertEqual(max_of_three(-1, -1, -1), -1)
        self.assertEqual(max_of_three(1, 2, 1), 2)
        self.assertEqual(max_of_three(-1, -2, -3), -1)
