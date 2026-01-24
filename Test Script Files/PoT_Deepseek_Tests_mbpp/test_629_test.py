import unittest
from mbpp_629_code import Split

class TestSplit(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(Split([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])

    def test_edge_cases(self):
        self.assertEqual(Split([]), [])
        self.assertEqual(Split([1]), [])
        self.assertEqual(Split([2]), [2])

    def test_boundary_cases(self):
        self.assertEqual(Split([1, 3, 5, 7, 9]), [])
        self.assertEqual(Split([0, 2, 4, 6, 8]), [0, 2, 4, 6, 8])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Split(123)
        with self.assertRaises(TypeError):
            Split("1,2,3,4,5")
        with self.assertRaises(TypeError):
            Split(None)
