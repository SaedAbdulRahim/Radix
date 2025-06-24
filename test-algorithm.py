import unittest
from algorithm import radix_sort_integers, radix_sort_strings

class TestRadixSort(unittest.TestCase):
    def test_integers(self):
        self.assertEqual(radix_sort_integers([170, 45, 75, 90, 802, 24, 2, 66]),
                         [2, 24, 45, 66, 75, 90, 170, 802])

    def test_strings(self):
        self.assertEqual(radix_sort_strings(["dog", "cat", "apple", "banana"]),
                         ['apple', 'banana', 'cat', 'dog'])

    def test_empty(self):
        self.assertEqual(radix_sort_integers([]), [])
        self.assertEqual(radix_sort_strings([]), [])

if __name__ == "__main__":
    unittest.main()

