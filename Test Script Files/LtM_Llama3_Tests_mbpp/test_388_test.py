import unittest
from mbpp_388_code import highest_Power_of_2

class TestHighestPowerOf2(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 4)
        self.assertEqual(highest_Power_of_2(6), 4)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(9), 8)
        self.assertEqual(highest_Power_of_2(10), 8)

    def test_edge(self):
        self.assertEqual(highest_Power_of_2(0), 0)
        self.assertEqual(highest_Power_of_2(1), 1)
        self.assertEqual(highest_Power_of_2(2), 2)
        self.assertEqual(highest_Power_of_2(3), 2)
        self.assertEqual(highest_Power_of_2(4), 4)
        self.assertEqual(highest_Power_of_2(5), 4)
        self.assertEqual(highest_Power_of_2(6), 4)
        self.assertEqual(highest_Power_of_2(7), 4)
        self.assertEqual(highest_Power_of_2(8), 8)
        self.assertEqual(highest_Power_of_2(9), 8)
        self.assertEqual(highest_Power_of_2(10), 8)

    def test_invalid(self):
        with self.assertRaises(TypeError):
            highest_Power_of_2("a")
        with self.assertRaises(TypeError):
            highest_Power_of_2(None)
        with self.assertRaises(TypeError):
            highest_Power_of_2(-1)
