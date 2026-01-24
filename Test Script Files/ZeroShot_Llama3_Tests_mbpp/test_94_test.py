import unittest
from mbpp_94_code import index_minimum

class TestIndexMinimum(unittest.TestCase):

    def test_index_minimum(self):
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2)]), "cherry")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10), ("kiwi", 11)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10), ("kiwi", 11), ("lemon", 12)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10), ("kiwi", 11), ("lemon", 12), ("mango", 13)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10), ("kiwi", 11), ("lemon", 12), ("mango", 13), ("nectarine", 14)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10), ("kiwi", 11), ("lemon", 12), ("mango", 13), ("nectarine", 14), ("orange", 15)]), "date")
        self.assertEqual(index_minimum([("apple", 5), ("banana", 3), ("cherry", 2), ("date", 1), ("elderberry", 4), ("fig", 6), ("grape", 7), ("honeydew", 8), ("ice cream", 9), ("jackfruit", 10), ("kiwi", 11