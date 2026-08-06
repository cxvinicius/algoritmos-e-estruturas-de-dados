from algoritmos.insertion_sort.insertion_sort import insertion_sort


def test_sort_unsorted_list():
    values = [7, 4, 5, 2]

    result = insertion_sort(values)

    assert result == [2, 4, 5, 7]


def test_sort_already_sorted_list():
    values = [1, 2, 3, 4, 5]

    result = insertion_sort(values)

    assert result == [1, 2, 3, 4, 5]


def test_sort_reverse_order_list():
    values = [5, 4, 3, 2, 1]

    result = insertion_sort(values)

    assert result == [1, 2, 3, 4, 5]


def test_sort_list_with_duplicates():
    values = [4, 2, 4, 1, 2]

    result = insertion_sort(values)

    assert result == [1, 2, 2, 4, 4]


def test_sort_empty_list():
    values = []

    result = insertion_sort(values)

    assert result == []


def test_original_list_is_not_modified():
    values = [7, 4, 5, 2]

    insertion_sort(values)

    assert values == [7, 4, 5, 2]