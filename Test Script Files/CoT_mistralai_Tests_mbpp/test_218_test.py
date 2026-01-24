import unittest
from mbpp_218_code import min_Operations

class TestMinOperations(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Operations(10, 20), 7)
        self.assertEqual(min_Operations(20, 10), 7)
        self.assertEqual(min_Operations(12, 16), 3)
        self.assertEqual(min_Operations(16, 12), 3)

    def test_edge_case_1(self):
        self.assertEqual(min_Operations(1, 1), 0)

    def test_edge_case_2(self):
        self.assertEqual(min_Operations(2, 1), 1)

    def test_edge_case_3(self):
        self.assertEqual(min_Operations(0, 1), 0)

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            min_Operations('a', 'b')

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            min_Operations([1, 2, 3], [4, 5, 6])
