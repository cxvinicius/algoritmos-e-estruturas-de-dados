from estruturas.hash_table.hash_table import HashTable
from estruturas.queue.queue_structure import Queue
from estruturas.stack.stack import Stack
from estruturas.tree.tree import BinarySearchTree
from projetos.mission_02_service_desk.models.ticket import Ticket


class ServiceDesk:
    def __init__(self):
        self.tickets = HashTable()
        self.waiting_tickets = Queue()
        self.status_history = Stack()
        self.ticket_ids = []
        self.next_ticket_number = 1


    def _generate_ticket_id(self):
        ticket_id = f"TCK-{self.next_ticket_number:03d}"
        self.next_ticket_number += 1
        return ticket_id


    def _validate_priority(self, priority):
        if priority not in Ticket.VALID_PRIORITIES:
            valid_priorities = ", ".join(Ticket.VALID_PRIORITIES)
            raise ValueError(
                f"Invalid priority: {priority}. Use: {valid_priorities}."
            )


    def _validate_status(self, status):
        if status not in Ticket.VALID_STATUSES:
            valid_statuses = ", ".join(Ticket.VALID_STATUSES)
            raise ValueError(
                f"Invalid status: {status}. Use: {valid_statuses}."
            )


    def _change_status(self, ticket, new_status):
        if ticket.status == new_status:
            return ticket

        previous_status = ticket.status
        ticket.status = new_status

        status_change = (
            ticket.ticket_id,
            previous_status,
        )
        self.status_history.push(status_change)

        return ticket


    def open_ticket(self, title, description, priority):
        self._validate_priority(priority)

        ticket_id = self._generate_ticket_id()
        new_ticket = Ticket(
            ticket_id,
            title,
            description,
            priority,
        )


        self.tickets.inserir(ticket_id, new_ticket)
        self.waiting_tickets.enqueue(ticket_id)
        self.ticket_ids.append(ticket_id)

        return new_ticket


    def find_ticket(self, ticket_id):
        return self.tickets.buscar(ticket_id)


    def attend_next_ticket(self):
        ticket_id = self.waiting_tickets.dequeue()

        if ticket_id is None:
            return None

        found_ticket = self.find_ticket(ticket_id)

        if found_ticket is None:
            return None

        return self._change_status(found_ticket, "in_progress")


    def update_status(self, ticket_id, new_status):
        self._validate_status(new_status)

        found_ticket = self.find_ticket(ticket_id)

        if found_ticket is None:
            return None

        return self._change_status(found_ticket, new_status)


    def undo_last_status_change(self):
        last_change = self.status_history.pop()

        if last_change is None:
            return None

        ticket_id, previous_status = last_change
        found_ticket = self.find_ticket(ticket_id)

        if found_ticket is None:
            return None

        found_ticket.status = previous_status
        return found_ticket


    def list_tickets(self):
        registered_tickets = []

        for ticket_id in self.ticket_ids:
            found_ticket = self.find_ticket(ticket_id)

            if found_ticket is not None:
                registered_tickets.append(found_ticket)

        return registered_tickets


    def get_priority_report(self):
        priority_order = {
            "low": 1,
            "medium": 2,
            "high": 3,
        }
        priority_tree = BinarySearchTree()

        for ticket in self.list_tickets():
            priority_rank = priority_order[ticket.priority]
            report_entry = (
                priority_rank,
                ticket.ticket_id,
                ticket,
            )
            priority_tree.insert(report_entry)

        ordered_entries = priority_tree.in_order()
        return [entry[2] for entry in ordered_entries]
