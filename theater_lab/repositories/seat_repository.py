from theater_lab.models import Seat
from django.db.models import Count



class SeatRepository:
    def get_all(self):
        return Seat.objects.all()

    def get_by_id(self, seat_id):
        return Seat.objects.get(id=seat_id)

    def create(self, seat_number, hall):
        seat = Seat(seat_number=seat_number, hall=hall)
        seat.save()
        return seat

def get_seat_occupancy_per_hall():
    return Seat.objects.values('hall__name').annotate(seat_count=Count('id')).order_by('seat_count')
