import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertEqual(unique_sublists([1]), {(1,): 1})

    def test_simple_list(self):
        self.assertEqual(unique_sublists([1, 2, 3]), {((1,),): 1, ((2,),): 1, ((3,),): 1, ((1, 2),): 2, ((1, 3),): 2, ((2, 3),): 2})

    def test_duplicate_sublists(self):
        self.assertEqual(unique_sublists([1, 2, [1, 2], 3]), {((1,),): 1, ((2,),): 1, (([1, 2],),): 1, ((3,),): 1, ((1, 2),): 2, ((1, 3),): 2, ((2, 3),): 2, (([1, 2], 3),): 2})

    def test_mixed_types(self):
        self.assertRaises(TypeError, unique_sublists, [1, 2, "a", [1, 2]])

    def test_nested_lists(self):
        self.assertEqual(unique_sublists([1, [2, [3]], 4]), {((1,),): 1, (([2, [3]],),): 1, (([3,],),): 1, ((4,),): 1, ((1, 2),): 2, ((1, [2, [3]]),): 2, ((1, 4),): 2, (([2, [3]], 4),): 2})
