import unittest
from mbpp_386_code import swap_count

class TestSwapCount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(swap_count('[]'), 0)
        self.assertEqual(swap_count('[[]]'), 0)
        self.assertEqual(swap_count('[[[]]]'), 0)

    def test_edge_cases(self):
        self.assertEqual(swap_count(''), 0)
        self.assertEqual(swap_count('[') , 0)
        self.assertEqual(swap_count(']'), 0)

    def test_imbalance_cases(self):
        self.assertEqual(swap_count('[[]'), 1)
        self.assertEqual(swap_count('[]['), 1)
        self.assertEqual(swap_count('[]][[]'), 2)
        self.assertEqual(swap_count('[[][][]'), 3)
        self.assertEqual(swap_count('[][][]]'), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            swap_count(123)
        with self.assertRaises(TypeError):
            swap_count({'[]'})
        with self.assertRaises(TypeError):
            swap_count([])
        with self.assertRaises(TypeError):
            swap_count(None)
