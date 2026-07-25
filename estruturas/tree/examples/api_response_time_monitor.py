from estruturas.tree.tree import BinarySearchTree


if __name__ == "__main__":
    response_times = [120, 85, 230, 95, 170, 60, 310]

    monitor = BinarySearchTree()

    for response_time in response_times:
        monitor.insert(response_time)

    ordered_response_times = monitor.in_order()
    minimum_response_time = monitor.find_min()
    maximum_response_time = monitor.find_max()

    searched_time = 170
    was_registered = monitor.search(searched_time)

    print("===== API RESPONSE TIME MONITOR =====\n")

    print("----- RESUMO -----")
    print(f"Quantidade de tempos registrados: {len(ordered_response_times)}")
    print(f"Menor tempo registrado: {minimum_response_time} ms")
    print(f"Maior tempo registrado: {maximum_response_time} ms\n")

    print("----- TEMPOS REGISTRADOS -----")
    print(f"{ordered_response_times}\n")

    print("----- CONSULTA -----")
    print(f"Tempo consultado: {searched_time} ms")

    if was_registered:
        print("Status: tempo registrado.")
    else:
        print("Status: tempo não registrado.")
