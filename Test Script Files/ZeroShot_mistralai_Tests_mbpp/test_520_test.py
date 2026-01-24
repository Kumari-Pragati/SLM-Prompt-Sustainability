import unittest
from mbpp_520_code import get_lcm, find_lcm

class TestGetLCM(unittest.TestCase):

    def test_get_lcm_single_pair(self):
        self.assertEqual(get_lcm([2, 4]), 8)
        self.assertEqual(get_lcm([1, 3]), 3)
        self.assertEqual(get_lcm([5, 10]), 50)
        self.assertEqual(get_lcm([15, 20]), 60)

    def test_get_lcm_multiple_pairs(self):
        self.assertEqual(get_lcm([2, 4, 6]), 24)
        self.assertEqual(get_lcm([1, 2, 3, 4]), 24)
        self.assertEqual(get_lcm([5, 10, 15]), 100)
        self.assertEqual(get_lcm([15, 20, 30]), 600)
