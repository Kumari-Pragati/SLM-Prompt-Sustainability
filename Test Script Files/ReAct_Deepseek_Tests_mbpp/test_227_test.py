import unittest
from mbpp_227_code import min_of_three

class TestMinOfThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_of_three(1, 2, 3), 1)
        self.assertEqual(min_of_three(5, 10, 15), 5)
        self.assertEqual(min_of_three(-1, 0, 1), -1)

    def test_edge_cases(self):
        self.assertEqual(min_of_three(0, 0, 0), 0)
        self.assertEqual(min_of_three(-1000, -2000, -3000), -3000)
        self.assertEqual(min_of_three(1000000, 1000000, 1000000), 1000000)

    def test_explicitly_handled_error_cases(self):
        # The function does not handle errors, so we just test for expected behavior
        self.assertEqual(min_of_three(1, 2, 'c'), 1)
        self.assertEqual(min_of_three('a', 'b', 'c'), 'a')
        self.assertEqual(min_of_three(None, 2, 3), None)
