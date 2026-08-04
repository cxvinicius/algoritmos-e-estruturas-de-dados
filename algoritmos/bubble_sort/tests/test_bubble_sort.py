from algoritmos.bubble_sort.bubble_sort import bubble_sort


def test_should_sort_unsorted_list():
    values = [5, 3, 8, 2]

    result = bubble_sort(values)

    assert result == [2, 3, 5, 8]


def test_should_keep_sorted_list():
    values = [1, 2, 3, 4]

    result = bubble_sort(values)

    assert result == [1, 2, 3, 4]


def test_should_sort_reverse_list():
    values = [5, 4, 3, 2, 1]

    result = bubble_sort(values)

    assert result == [1, 2, 3, 4, 5]


def test_should_sort_list_with_duplicate_values():
    values = [4, 2, 4, 1, 2]

    result = bubble_sort(values)

    assert result == [1, 2, 2, 4, 4]


def test_should_return_empty_list():
    values = []

    result = bubble_sort(values)

    assert result == []


def test_should_return_single_element_list():
    values = [10]

    result = bubble_sort(values)

    assert result == [10]


def test_should_not_modify_original_list():
    values = [5, 3, 8, 2]

    bubble_sort(values)

    assert values == [5, 3, 8, 2]