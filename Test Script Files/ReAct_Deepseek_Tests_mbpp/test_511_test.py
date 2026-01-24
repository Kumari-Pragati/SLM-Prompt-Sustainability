import unittest
from mbpp_511_code import find_Min_Sum

class TestFindMinSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Min_Sum(12), 10)
        self.assertEqual(find_Min_Sum(15), 15)
        self.assertEqual(find_Min_Sum(27), 27)
        self.assertEqual(find_Min_Sum(100), 100)

    def test_edge_cases(self):
        self.assertEqual(find_Min_Sum(1), 1)
        self.assertEqual(find_Min_Sum(0), 0)
        self.assertEqual(find_Min_Sum(2), 2)
        self.assertEqual(find_Min_Sum(3), 3)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            find_Min_Sum('12')
        with self.assertRaises(TypeError):
            find_Min_Sum(None)
        with self.assertRaises(TypeError):
            find_Min_Sum([])
