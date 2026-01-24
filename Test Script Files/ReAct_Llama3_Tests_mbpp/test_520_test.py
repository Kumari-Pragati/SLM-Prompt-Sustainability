import unittest
from mbpp_520_code import get_lcm

class TestGetLcm(unittest.TestCase):

    def test_single_pair(self):
        self.assertEqual(get_lcm([1, 2]), 2)

    def test_multiple_pairs(self):
        self.assertEqual(get_lcm([1, 2, 3, 4]), 12)

    def test_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12]), 12)

    def test_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24]), 24)

    def test_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36]), 36)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48]), 48)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48, 60]), 60)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48, 60, 72]), 72)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48, 60, 72, 84]), 84)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48, 60, 72, 84, 96]), 96)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48, 60, 72, 84, 96, 108]), 108)

    def test_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm_of_lcm(self):
        self.assertEqual(get_lcm([2, 3, 6, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120]), 120)
