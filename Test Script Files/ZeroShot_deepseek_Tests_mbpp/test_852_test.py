import unittest
from mbpp_852_code import remove_negs

class TestRemoveNegs(unittest.TestCase):

    def test_remove_negs(self):
        self.assertEqual(remove_negs([1, -2, 3, -4, 5]), [1, 3, 5])
        self.assertEqual(remove_negs([-1, -2, -3, -4, -5]), [])
        self.assertEqual(remove_negs([0, -1, 2, -3, 4]), [0, 2, 4])
        self.assertEqual(remove_negs([1]), [1])
        self.assertEqual(remove_negs([]), [])
