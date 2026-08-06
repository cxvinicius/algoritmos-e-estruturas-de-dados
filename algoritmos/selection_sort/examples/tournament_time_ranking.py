from algoritmos.selection_sort.selection_sort import selection_sort

if __name__ == "__main__":
    race_times = [30, 34, 56, 60, 45, 23, 29]

    sorted_race_times = selection_sort(race_times)

    print("===== TOURNAMENT TIME RANKING =====")
    print()

    print("Recorded times:")

    for time in race_times:
        print(f"{time} seconds")

    print()

    print("Ranking from fastest to slowest:")

    for position, time in enumerate(sorted_race_times, start=1):
        print(f"{position}. {time} seconds")







