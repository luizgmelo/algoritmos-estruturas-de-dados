import pytest
import random
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

@pytest.mark.parametrize("algorithm", [(bubble_sort),(selection_sort),(insertion_sort),(shell_sort),(merge_sort),(quick_sort)])
def test_sorting_random_numbers(algorithm):
    random_numbers = random.sample(range(100), 100)
    result = algorithm(random_numbers)
    assert result == list(range(100))

@pytest.mark.parametrize("algorithm", [(bubble_sort), (selection_sort),(insertion_sort),(shell_sort),(merge_sort),(quick_sort)])
def test_sorting_reverse_numbers(algorithm):
    reverse_numbers = list(range(99, -1, -1))
    result = algorithm(reverse_numbers)
    assert result == list(range(100))

@pytest.mark.parametrize("algorithm", [(bubble_sort), (selection_sort),(insertion_sort),(shell_sort),(merge_sort),(quick_sort)])
def test_sorting_order_numbers(algorithm):
    order_numbers = list(range(100))
    result = algorithm(order_numbers)
    assert result == order_numbers


@pytest.mark.parametrize("algorithm", [(bubble_sort), (selection_sort),(insertion_sort),(shell_sort),(merge_sort),(quick_sort)])
def test_sorting_repeated_numbers(algorithm):
    repeated_numbers = [7, 7, 7, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 5, 5, 6, 6, 6, 4, 4]
    result = algorithm(repeated_numbers)
    assert result == [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7]

