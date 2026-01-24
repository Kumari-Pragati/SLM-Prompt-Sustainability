import unittest
from mbpp_2_code import similar_elements

class TestSimilarElements(unittest.TestCase):

    def test_similar_elements_empty_tuples(self):
        self.assertSetEqual(similar_elements((), ()), set())

    def test_similar_elements_single_element_tuples(self):
        self.assertSetEqual(similar_elements((1,), (1,)), {(1,)})
        self.assertSetEqual(similar_elements((1,), (2,)), set())

    def test_similar_elements_identical_tuples(self):
        self.assertSetEqual(similar_elements((1, 2, 3), (1, 2, 3)), {(1, 2, 3)})

    def test_similar_elements_different_order_tuples(self):
        self.assertSetEqual(similar_elements((1, 2, 3), (3, 2, 1)), {(1, 2, 3)})

    def test_similar_elements_same_elements_different_types(self):
        self.assertSetEqual(similar_elements((1, 'a'), (1, 'b')), {(1,)})

    def test_similar_elements_different_elements(self):
        self.assertSetEqual(similar_elements((1, 2, 3), (4, 5, 6)), set())

    def test_similar_elements_one_set_empty(self):
        self.assertSetEqual(similar_elements((1, 2, 3), ()), set())

    def test_similar_elements_one_set_single_element(self):
        self.assertSetEqual(similar_elements((1, 2, 3), (4,)), set())
