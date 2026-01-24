import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(odd_Days(1), 0)
        self.assertEqual(odd_Days(2), 1)
        self.assertEqual(odd_Days(3), 1)
        self.assertEqual(odd_Days(4), 2)
        self.assertEqual(odd_Days(5), 3)
        self.assertEqual(odd_Days(6), 4)
        self.assertEqual(odd_Days(7), 5)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(100), 0)
        self.assertEqual(odd_Days(400), 0)
        self.assertEqual(odd_Days(1000), 0)
        self.assertEqual(odd_Days(1001), 1)
        self.assertEqual(odd_Days(1002), 2)
        self.assertEqual(odd_Days(1003), 3)
        self.assertEqual(odd_Days(1004), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            odd_Days('a')
        with self.assertRaises(TypeError):
            odd_Days(None)
        with self.assertRaises(TypeError):
            odd_Days(100.5)
