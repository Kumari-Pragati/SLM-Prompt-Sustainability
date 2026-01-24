import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(frequency([1, 2, 3, 1, 2, 3], 1), 3)
        self.assertEqual(frequency(["a", "b", "a", "c", "a"], "a"), 3)

    def test_edge_cases(self):
        self.assertEqual(frequency([], 1), 0)
        self.assertEqual(frequency([1], 1), 1)
        self.assertEqual(frequency([1, 1], 1), 2)
        self.assertEqual(frequency(["a", "b"], "a"), 1)
        self.assertEqual(frequency(["a", "a"], "a"), 2)

    def test_boundary_cases(self):
        self.assertEqual(frequency([-1, 0, 1], 0), 1)
        self.assertEqual(frequency(["z", "a", "z"], "z"), 2)

    def test_invalid_input(self):
        self.assertRaises(TypeError, frequency, [1, 2, 3], 1.5)
        self.assertRaises(TypeError, frequency, ["a", "b", "c"], 1 + 2j)
