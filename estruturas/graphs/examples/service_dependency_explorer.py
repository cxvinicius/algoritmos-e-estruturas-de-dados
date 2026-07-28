from estruturas.graphs.graph import Graph

def main():
    services = Graph(directed=True)

    services.add_edge("API Gateway", "Auth Service")
    services.add_edge("API Gateway", "Order Service")
    services.add_edge("API Gateway", "User Service")
    services.add_edge("Order Service", "Payment Service")
    services.add_edge("Order Service", "Inventory Service")

    print("===== SERVICE DEPENDENCY EXPLORER =====")
    print()

    print("Service dependencies:")
    print(services)
    print()

    print("===== CHECKS =====")
    print()

    print(f"Payment Service exists: {services.has_vertex('Payment Service')}")
    print(f"Notification Service exists: {services.has_vertex('Notification Service')}")

    print(f"Order Service depends on Payment Service: {services.has_edge('Order Service', 'Payment Service')}")
    print(f"Payment Service depends on Order Service: {services.has_edge('Payment Service', 'Order Service')}")
    print()

    print("Direct dependencies of API Gateway:")
    dependencies = services.get_neighbors("API Gateway")
    print(", ".join(sorted(dependencies)))
    print()

    print("===== TRAVERSALS =====")
    print()

    print("BFS from API Gateway:")
    print(services.breadth_first_search("API Gateway"))
    print()

    print("DFS from API Gateway:")
    print(services.depth_first_search("API Gateway"))
    print()

    print("BFS from non-existent service (Ghost Service):")
    print(services.breadth_first_search("Ghost Service"))


if __name__ == "__main__":
    main()





