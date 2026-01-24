import unittest
from mbpp_77_code import is_Diff

class TestIsDiff(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_Diff(11))
        self.assertTrue(is_Diff(22))
        self.assertTrue(is_Diff(33))
        self.assertTrue(is_Diff(44))
        self.assertTrue(is_Diff(55))
        self.assertTrue(is_Diff(66))
        self.assertTrue(is_Diff(77))
        self.assertTrue(is_Diff(88))
        self.assertTrue(is_Diff(99))
        self.assertTrue(is_Diff(110))

    def test_edge_cases(self):
        self.assertFalse(is_Diff(0))
        self.assertFalse(is_Diff(1))
        self.assertFalse(is_Diff(2))
        self.assertFalse(is_Diff(3))
        self.assertFalse(is_Diff(4))
        self.assertFalse(is_Diff(5))
        self.assertFalse(is_Diff(6))
        self.assertFalse(is_Diff(7))
        self.assertFalse(is_Diff(8))
        self.assertFalse(is_Diff(9))
        self.assertFalse(is_Diff(10))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_Diff('11')
        with self.assertRaises(TypeError):
            is_Diff(None)
        with self.assertRaises(TypeError):
            is_Diff([])
        with self.assertRaises(TypeError):
            is_Diff({})
