import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):
    def test_find_extra(self):
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 5), 5)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 7], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 8], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 9], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 10], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 11], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 12], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 13], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 14], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 15], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 16], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 17], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 18], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 19], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 20], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 21], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 22], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 23], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 24], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 25], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 26], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4, 27], 5), 4)
        self.assertEqual(find_Extra([1, 2, 3, 4, 5], [1, 2, 3, 4