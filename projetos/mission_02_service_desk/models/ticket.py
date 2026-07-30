class Ticket:
    VALID_PRIORITIES = ("low", "medium", "high")
    VALID_STATUSES = ("waiting", "in_progress", "resolved")

    def __init__(self, ticket_id, title, description, priority):
        self.ticket_id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "waiting"

    def __str__(self):
        return (
            f"[{self.ticket_id}] {self.title} | "
            f"Priority: {self.priority} | Status: {self.status}"
        )
