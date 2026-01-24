import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 3], [1, 2]]), {(1, 2): 2, (2, 3): 1})
        self.assertEqual(unique_sublists([[1, 2, 3], [2, 3, 4], [1, 2, 3], [4, 5, 6]]), {(1, 2, 3): 2, (2, 3, 4): 1, (4, 5, 6): 1})
        self.assertEqual(unique_sublists([[1, 2, 3], [1, 2, 3]]), {(1, 2, 3): 2})
        self.assertEqual(unique_sublists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), {(1, 2, 3): 1, (4, 5, 6): 1, (7, 8, 9): 1})
        self.assertEqual(unique_sublists([]), {})
