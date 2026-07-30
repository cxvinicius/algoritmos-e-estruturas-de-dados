from projetos.mission_02_service_desk.core.service_desk import ServiceDesk


def main():
    service_desk = ServiceDesk()

    print("===== SERVICE DESK =====\n")

    database_ticket = service_desk.open_ticket(
        "Database connection error",
        "The application cannot connect to the database.",
        "high",
    )
    service_desk.open_ticket(
        "System access request",
        "A new employee needs access to the internal system.",
        "low",
    )
    service_desk.open_ticket(
        "Printer unavailable",
        "The finance department cannot use the network printer.",
        "medium",
    )

    print("Opened tickets:")
    for ticket in service_desk.list_tickets():
        print(f"- {ticket}")

    print("\nTicket search:")
    print(service_desk.find_ticket(database_ticket.ticket_id))

    print("\nNext ticket in attendance:")
    attended_ticket = service_desk.attend_next_ticket()
    print(attended_ticket)

    print("\nStatus update:")
    resolved_ticket = service_desk.update_status(
        attended_ticket.ticket_id,
        "resolved",
    )
    print(resolved_ticket)

    print("\nUndo last status change:")
    restored_ticket = service_desk.undo_last_status_change()
    print(restored_ticket)

    print("\nPriority report (ascending):")
    for ticket in service_desk.get_priority_report():
        print(f"- {ticket.priority}: {ticket.ticket_id} — {ticket.title}")



if __name__ == "__main__":
    main()
