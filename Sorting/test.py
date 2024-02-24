import unittest
import random
from bubble_sort import bubble_sort
from selection_sort import selection_sort


class TestSortingAlgorithms(unittest.TestCase):
    # Uncomment for test Algorithm
    ALG = []
    ALG.append(bubble_sort)
    # ALG.append(selection_sort)

    def test_sorting_random_numbers(self):
        random_numbers = random.sample(range(100), 100)
        result = self.ALG[0](random_numbers)
        self.assertEqual(result, list(range(100)))

    def test_sorting_reverse_numbers(self):
        reverse_numbers = list(range(99, -1, -1))
        result = self.ALG[0](reverse_numbers)
        self.assertEqual(result, list(range(100)))

    def test_sorting_order_numbers(self):
        order_numbers = list(range(100))
        result = self.ALG[0](order_numbers)
        self.assertEqual(result, order_numbers)

if __name__ == '__main__':
    unittest.main()
