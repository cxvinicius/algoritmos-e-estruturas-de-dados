def insertion_sort(values):
    sorted_values = values.copy()

    for current_index in range(1, len(sorted_values)):
        current_value = sorted_values[current_index]
        previous_index = current_index - 1

        while (
            previous_index >= 0
            and sorted_values[previous_index] > current_value
        ):
            sorted_values[previous_index + 1] = sorted_values[previous_index]
            previous_index -= 1

        sorted_values[previous_index + 1] = current_value

    return sorted_values

