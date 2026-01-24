import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(5, 1), 5)
        self.assertEqual(find(0, 1), 0)
        self.assertEqual(find(1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(find(-10, 2), -5)
        self.assertEqual(find(10, 0), 0)
        self.assertEqual(find(0, 0), 0)
        self.assertEqual(find(10, 10), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find('a', 2)
        with self.assertRaises(TypeError):
            find(10, 'b')
