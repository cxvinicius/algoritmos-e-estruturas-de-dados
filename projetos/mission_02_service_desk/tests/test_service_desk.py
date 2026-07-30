import pytest

from projetos.mission_02_service_desk.core.service_desk import ServiceDesk


def test_open_ticket_stores_and_queues_ticket():
    service_desk = ServiceDesk()

    created_ticket = service_desk.open_ticket(
        "Database error",
        "The application cannot connect.",
        "high",
    )

    assert created_ticket.ticket_id == "TCK-001"
    assert created_ticket.status == "waiting"
    assert service_desk.find_ticket("TCK-001") is created_ticket
    assert len(service_desk.waiting_tickets) == 1


def test_find_ticket_returns_none_when_id_does_not_exist():
    service_desk = ServiceDesk()

    assert service_desk.find_ticket("TCK-999") is None


def test_attend_next_ticket_respects_fifo_order():
    service_desk = ServiceDesk()
    first_ticket = service_desk.open_ticket("First", "First ticket", "low")
    service_desk.open_ticket("Second", "Second ticket", "high")

    attended_ticket = service_desk.attend_next_ticket()

    assert attended_ticket is first_ticket
    assert attended_ticket.status == "in_progress"
    assert len(service_desk.waiting_tickets) == 1


def test_attend_next_ticket_returns_none_when_queue_is_empty():
    service_desk = ServiceDesk()

    assert service_desk.attend_next_ticket() is None


def test_update_status_changes_existing_ticket():
    service_desk = ServiceDesk()
    created_ticket = service_desk.open_ticket("Access", "Access request", "medium")

    updated_ticket = service_desk.update_status(
        created_ticket.ticket_id,
        "resolved",
    )

    assert updated_ticket is created_ticket
    assert updated_ticket.status == "resolved"
    assert service_desk.status_history.size() == 1


def test_update_status_returns_none_for_unknown_ticket():
    service_desk = ServiceDesk()

    assert service_desk.update_status("TCK-999", "resolved") is None
    assert service_desk.status_history.is_empty()


def test_undo_last_status_change_restores_previous_status():
    service_desk = ServiceDesk()
    created_ticket = service_desk.open_ticket("Printer", "Printer error", "low")
    service_desk.update_status(created_ticket.ticket_id, "in_progress")
    service_desk.update_status(created_ticket.ticket_id, "resolved")

    restored_ticket = service_desk.undo_last_status_change()

    assert restored_ticket is created_ticket
    assert restored_ticket.status == "in_progress"
    assert service_desk.status_history.size() == 1


def test_undo_returns_none_when_history_is_empty():
    service_desk = ServiceDesk()

    assert service_desk.undo_last_status_change() is None


def test_list_tickets_returns_all_registered_tickets():
    service_desk = ServiceDesk()
    first_ticket = service_desk.open_ticket("First", "Description", "low")
    second_ticket = service_desk.open_ticket("Second", "Description", "high")

    assert service_desk.list_tickets() == [first_ticket, second_ticket]


def test_priority_report_orders_tickets_and_preserves_duplicates():
    service_desk = ServiceDesk()
    high_ticket = service_desk.open_ticket("High", "Description", "high")
    low_ticket = service_desk.open_ticket("Low", "Description", "low")
    second_high_ticket = service_desk.open_ticket(
        "Second high",
        "Description",
        "high",
    )
    medium_ticket = service_desk.open_ticket("Medium", "Description", "medium")

    report = service_desk.get_priority_report()

    assert report == [
        low_ticket,
        medium_ticket,
        high_ticket,
        second_high_ticket,
    ]


@pytest.mark.parametrize("invalid_priority", ["urgent", "LOW", ""])
def test_open_ticket_rejects_invalid_priority(invalid_priority):
    service_desk = ServiceDesk()

    with pytest.raises(ValueError):
        service_desk.open_ticket("Invalid", "Description", invalid_priority)


@pytest.mark.parametrize("invalid_status", ["closed", "OPEN", ""])
def test_update_status_rejects_invalid_status(invalid_status):
    service_desk = ServiceDesk()
    created_ticket = service_desk.open_ticket("Valid", "Description", "low")

    with pytest.raises(ValueError):
        service_desk.update_status(created_ticket.ticket_id, invalid_status)
