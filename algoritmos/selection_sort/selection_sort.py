def selection_sort(values):
    sorted_values = values.copy()

    for current_index in range(len(sorted_values) - 1):
        min_index = current_index

        for comparison_index in range(
            current_index + 1,
            len(sorted_values),
        ):
            if sorted_values[comparison_index] < sorted_values[min_index]:
                min_index = comparison_index

        if min_index != current_index:
            sorted_values[current_index], sorted_values[min_index] = (
                sorted_values[min_index],
                sorted_values[current_index],
            )

    return sorted_values