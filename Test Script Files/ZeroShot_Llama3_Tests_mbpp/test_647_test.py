import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperString(unittest.TestCase):

    def test_split_upperstring(self):
        self.assertEqual(split_upperstring("HelloWorld"), ["Hello", "World"])
        self.assertEqual(split_upperstring("HelloWorld123"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World456"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World456789"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABC"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF123"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF123456"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF123456789"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABC"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF123"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF123456"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF123456789"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABC"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF123"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF123456"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF123456789"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABC"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF123"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF123456"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF123456789"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABC"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"), ["Hello", "World"])
        self.assertEqual(split_upperstring("Hello123World4567890ABCDEF123