import unittest
from mbpp_211_code import count_Num

class TestCount_Num(unittest.TestCase):

    def test_count_Num_typical(self):
        self.assertEqual(count_Num(2), 2)
        self.assertEqual(count_Num(3), 4)
        self.assertEqual(count_Num(4), 8)

    def test_count_Num_edge(self):
        self.assertEqual(count_Num(1), 1)
        self.assertEqual(count_Num(5), 16)

    def test_count_Num_error(self):
        with self.assertRaises(TypeError):
            count_Num('a')
