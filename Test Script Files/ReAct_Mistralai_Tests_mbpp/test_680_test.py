import unittest
from mbpp_680_code import increasing_trend

class TestIncreasingTrend(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(increasing_trend([]))

    def test_single_element(self):
        for num in range(10):
            self.assertTrue(increasing_trend([num]))

    def test_increasing_sequence(self):
        for i in range(1, 10):
            self.assertTrue(increasing_trend(list(range(i))))

    def test_decreasing_sequence(self):
        for i in range(1, 10):
            self.assertFalse(increasing_trend(list(reversed(range(i)))))

    def test_duplicate_elements(self):
        for i in range(1, 10):
            self.assertFalse(increasing_trend(list(range(i)) + [i] + list(range(i))))

    def test_mixed_sequence(self):
        for i in range(1, 10):
            self.assertFalse(increasing_trend(list(range(i)) + list(reversed(range(i, 10))) + [i]))
