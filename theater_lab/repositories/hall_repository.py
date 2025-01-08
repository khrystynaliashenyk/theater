from theater_lab.models import Hall

class HallRepository:
    def get_all(self):
        return Hall.objects.all()

    def get_by_id(self, hall_id):
        return Hall.objects.get(id=hall_id)

    def create(self, name, number_of_seats, theatre):
        hall = Hall(name=name, number_of_seats=number_of_seats, theatre=theatre)
        hall.save()
        return hall