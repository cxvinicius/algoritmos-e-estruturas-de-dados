def bubble_sort(values):
    sorted_values = values.copy()

    for pass_index in range(len(sorted_values) - 1):
        swapped = False

        for current_index in range(len(sorted_values) - 1 - pass_index):
            if sorted_values[current_index] > sorted_values[current_index + 1]:
                sorted_values[current_index], sorted_values[current_index + 1] = (
                    sorted_values[current_index + 1],
                    sorted_values[current_index],
                )

                swapped = True

        if not swapped:
            break

    return sorted_values