import unittest
from mbpp_672_code import max_of_three

class TestMaxOfThree(unittest.TestCase):

    def test_max_of_three(self):
        self.assertEqual(max_of_three(1, 2, 3), 3)
        self.assertEqual(max_of_three(3, 2, 1), 3)
        self.assertEqual(max_of_three(2, 3, 1), 3)
        self.assertEqual(max_of_three(1, 3, 2), 3)
        self.assertEqual(max_of_three(2, 2, 2), 2)
        self.assertEqual(max_of_three(-1, -2, -3), -1)
        self.assertEqual(max_of_three(-3, -2, -1), -1)
        self.assertEqual(max_of_three(-2, -1, -3), -1)
        self.assertEqual(max_of_three(-1, -3, -2), -1)
        self.assertEqual(max_of_three(0, 0, 0), 0)
