from algoritmos.selection_sort.selection_sort import selection_sort


def test_selection_sort_orders_unsorted_values():
    values = [64, 25, 12, 22, 11]

    result = selection_sort(values)

    assert result == [11, 12, 22, 25, 64]


def test_selection_sort_keeps_sorted_values():
    values = [10, 20, 30, 40, 50]

    result = selection_sort(values)

    assert result == [10, 20, 30, 40, 50]


def test_selection_sort_orders_values_in_reverse_order():
    values = [50, 40, 30, 20, 10]

    result = selection_sort(values)

    assert result == [10, 20, 30, 40, 50]


def test_selection_sort_handles_duplicate_values():
    values = [4, 2, 4, 1, 2]

    result = selection_sort(values)

    assert result == [1, 2, 2, 4, 4]


def test_selection_sort_handles_empty_list():
    values = []

    result = selection_sort(values)

    assert result == []


def test_selection_sort_handles_single_value():
    values = [7]

    result = selection_sort(values)

    assert result == [7]


def test_selection_sort_preserves_original_list():
    values = [30, 10, 20]
    original_values = values.copy()

    selection_sort(values)

    assert values == original_values
