import pytest
import random
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from shell_sort import shell_sort

@pytest.mark.parametrize("algorithm", [(bubble_sort),(selection_sort),(insertion_sort),(shell_sort)])
def test_sorting_random_numbers(algorithm):
    random_numbers = random.sample(range(100), 100)
    result = algorithm(random_numbers)
    assert result == list(range(100))

@pytest.mark.parametrize("algorithm", [(bubble_sort), (selection_sort),(insertion_sort),(shell_sort)])
def test_sorting_reverse_numbers(algorithm):
    reverse_numbers = list(range(99, -1, -1))
    result = algorithm(reverse_numbers)
    assert result == list(range(100))

@pytest.mark.parametrize("algorithm", [(bubble_sort), (selection_sort),(insertion_sort),(shell_sort)])
def test_sorting_order_numbers(algorithm):
    order_numbers = list(range(100))
    result = algorithm(order_numbers)
    assert result == order_numbers

