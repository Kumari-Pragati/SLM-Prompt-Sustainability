import unittest
from758_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(unique_sublists([1]), {(1,): 1})

    def test_duplicate_elements_list(self):
        self.assertDictEqual(unique_sublists([1, 1, 2, 2]), {((1,),): 2, ((2,),): 2})

    def test_unique_elements_list(self):
        self.assertDictEqual(unique_sublists([1, 2, 3]), {((1,),): 1, ((2,),): 1, ((3,),): 1})

    def test_mixed_elements_list(self):
        self.assertDictEqual(unique_sublists([1, 1, 2, 2, 3, 3, 4, 4, 5]), {
            ((1,),): 2,
            ((2,),): 2,
            ((3,),): 2,
            ((4,),): 2,
            ((5,),): 1
        })
