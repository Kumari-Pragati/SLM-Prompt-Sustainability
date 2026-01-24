import unittest
from mbpp_457_code import Find_Min

class TestFind_Min(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(Find_Min([10, 20, 30, 40, 50]), 10)
        self.assertEqual(Find_Min([-10, -20, -30, -40, -50]), -50)
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(Find_Min([0, 0, 0, 0, 0]), 0)
        self.assertEqual(Find_Min([-10, -20, 0, 30, 40]), 0)
        self.assertEqual(Find_Min([-10, -20, 0, 30, 40, 50]), 0)
        self.assertEqual(Find_Min([10, 20, 30, 40, 50, 60]), 10)
        self.assertEqual(Find_Min([-10, -20, -30, -40, -50, -60]), -60)
