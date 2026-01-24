import unittest
from mbpp_554_code import Split

class TestSplit(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(Split([10, 20, 30, 40, 50]), [])
        self.assertEqual(Split([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

    def test_edge_cases(self):
        self.assertEqual(Split([0]), [])
        self.assertEqual(Split([]), [])

    def test_boundary_cases(self):
        self.assertEqual(Split([2]), [])
        self.assertEqual(Split([1]), [1])

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Split("1,2,3")
        with self.assertRaises(TypeError):
            Split("abc")
        with self.assertRaises(TypeError):
            Split(123)
