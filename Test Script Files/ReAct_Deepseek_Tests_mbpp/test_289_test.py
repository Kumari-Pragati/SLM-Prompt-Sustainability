import unittest
from mbpp_289_code import odd_Days

class TestOddDays(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(odd_Days(1980), 1)
        self.assertEqual(odd_Days(2000), 3)
        self.assertEqual(odd_Days(2021), 1)

    def test_edge_cases(self):
        self.assertEqual(odd_Days(0), 0)
        self.assertEqual(odd_Days(1752), 2)
        self.assertEqual(odd_Days(9999), 0)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            odd_Days('2021')
        with self.assertRaises(ValueError):
            odd_Days(-1)
