import unittest
from mbpp_810_code import Counter
from mbpp_810_code import count_variable

class TestCountVariable(unittest.TestCase):

    def test_count_variable(self):
        self.assertEqual(count_variable(1, 2, 3, 4), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(0, 0, 0, 0), [])
        self.assertEqual(count_variable(1, 2, 3, 4), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(5, 5, 5, 5), ['p', 'q', 'r', 's'])
        self.assertEqual(count_variable(10, 20, 30, 40), ['p', 'q', 'r', 's'])
