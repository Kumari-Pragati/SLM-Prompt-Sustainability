import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertDictEqual(unique_sublists([]), {})

    def test_single_element_list(self):
        self.assertDictEqual(unique_sublists([1]), {(1,): 1})

    def test_duplicate_elements(self):
        self.assertDictEqual(unique_sublists([1, 1, 2, 2, 3]), {((1,),): 2, ((2,),): 2, ((3,),): 1})

    def test_unique_elements(self):
        self.assertDictEqual(unique_sublists([1, 2, 3]), {((1,),): 1, ((2,),): 1, ((3,),): 1})

    def test_mixed_elements(self):
        self.assertDictEqual(unique_sublists([1, 1, 2, 2, 3, 4]), {((1,),): 2, ((2,),): 2, ((3,),): 1, ((4,),): 1})
