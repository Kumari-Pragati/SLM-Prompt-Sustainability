import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(odd_Days(1), 1)
        self.assertEqual(odd_Days(2), 3)
        self.assertEqual(odd_Days(3), 5)
        self.assertEqual(odd_Days(4), 0)
        self.assertEqual(odd_Days(5), 2)
        self.assertEqual(odd_Days(6), 4)
        self.assertEqual(odd_Days(7), 6)
        self.assertEqual(odd_Days(8), 1)
        self.assertEqual(odd_Days(9), 3)
        self.assertEqual(odd_Days(10), 5)

    def test_edge_conditions(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(100), 1)
        self.assertEqual(odd_Days(365), 1)
        self.assertEqual(odd_Days(366), 0)
        self.assertEqual(odd_Days(367), 1)
        self.assertEqual(odd_Days(400), 1)
        self.assertEqual(odd_Days(800), 1)

    def test_complex_cases(self):
        self.assertEqual(odd_Days(1000), 1)
        self.assertEqual(odd_Days(1001), 3)
        self.assertEqual(odd_Days(1002), 5)
        self.assertEqual(odd_Days(1003), 0)
        self.assertEqual(odd_Days(1004), 2)
        self.assertEqual(odd_Days(1005), 4)
        self.assertEqual(odd_Days(1006), 6)
        self.assertEqual(odd_Days(1007), 1)
        self.assertEqual(odd_Days(1008), 3)
        self.assertEqual(odd_Days(1009), 5)
