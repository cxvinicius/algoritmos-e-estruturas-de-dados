from algoritmos.insertion_sort.insertion_sort import insertion_sort


if __name__ == "__main__":
    check_in_times = [
        "08:00",
        "08:03",
        "08:06",
        "08:10",
        "08:08",
        "08:12",
        "08:15",
    ]

    sorted_check_in_times = insertion_sort(check_in_times)

    print("===== CONFERENCE CHECK-IN ORGANIZER =====")
    print()

    print("Recorded check-ins:")
    for check_in_time in check_in_times:
        print(check_in_time)

    print()

    print("Check-ins in chronological order:")
    for position, check_in_time in enumerate(sorted_check_in_times, start=1):
        print(f"{position}. {check_in_time}")