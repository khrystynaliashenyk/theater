from theater_lab.models import Ticket

class TicketRepository:
    def get_all(self):
        return Ticket.objects.all()

    def get_by_id(self, ticket_id):
        return Ticket.objects.get(id=ticket_id)

    def create(self, ticket_number, seat, buyer, price, schedule):
        ticket = Ticket(ticket_number=ticket_number, seat=seat, buyer=buyer, price=price, schedule=schedule)
        ticket.save()
        return ticket