from algoritmos.bubble_sort.bubble_sort import bubble_sort

if __name__ == "__main__":
    exam_scores = [7.5, 5.0, 9.0, 6.5, 8.0, 4.5, 3.0]

    sorted_exam_scores  = bubble_sort(exam_scores)

    print("===== EXAM SCORE ORGANIZER =====")
    print()

    print("Original scores:")
    print(*exam_scores, sep=" | ")

    print()

    print("Sorted scores:")
    print(*sorted_exam_scores, sep=" | ")
