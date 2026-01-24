import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_find_remainder(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 1)
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 2)
        self.assertEqual(find_remainder([1, 2, 3], 3, 7), 3)
        self.assertEqual(find_remainder([1, 2, 3], 3, 11), 4)
        self.assertEqual(find_remainder([1, 2, 3], 3, 13), 6)
        self.assertEqual(find_remainder([1, 2, 3], 3, 17), 7)
        self.assertEqual(find_remainder([1, 2, 3], 3, 19), 9)
        self.assertEqual(find_remainder([1, 2, 3], 3, 23), 12)
        self.assertEqual(find_remainder([1, 2, 3], 3, 29), 16)
        self.assertEqual(find_remainder([1, 2, 3], 3, 31), 18)
        self.assertEqual(find_remainder([1, 2, 3], 3, 37), 21)
        self.assertEqual(find_remainder([1, 2, 3], 3, 41), 24)
        self.assertEqual(find_remainder([1, 2, 3], 3, 43), 27)
        self.assertEqual(find_remainder([1, 2, 3], 3, 47), 30)
        self.assertEqual(find_remainder([1, 2, 3], 3, 53), 33)
        self.assertEqual(find_remainder([1, 2, 3], 3, 59), 36)
        self.assertEqual(find_remainder([1, 2, 3], 3, 61), 39)
        self.assertEqual(find_remainder([1, 2, 3], 3, 67), 42)
        self.assertEqual(find_remainder([1, 2, 3], 3, 71), 45)
        self.assertEqual(find_remainder([1, 2, 3], 3, 73), 48)
        self.assertEqual(find_remainder([1, 2, 3], 3, 79), 51)
        self.assertEqual(find_remainder([1, 2, 3], 3, 83), 54)
        self.assertEqual(find_remainder([1, 2, 3], 3, 89), 57)
        self.assertEqual(find_remainder([1, 2, 3], 3, 97), 60)
