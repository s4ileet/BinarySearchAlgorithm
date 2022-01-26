import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_area(self):
        self.assertEqual(binary_search([0, 1, 2, 3, 4], 1), (1, 1))
        self.assertEqual(binary_search([14, 122, 23, 333, 42], 42), (42, 2))
        self.assertEqual(binary_search([0], 1), (1, -1))

    def test_types(self):
        self.assertRaises(TypeError, binary_search, ['aaa'])
        self.assertRaises(TypeError, binary_search, ['string', '3', 'a'])