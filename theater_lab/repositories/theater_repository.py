from theater_lab.models import Theater

class TheaterRepository:
    def get_all(self):
        return Theater.objects.all()

    def get_by_id(self, theater_id):
        return Theater.objects.get(id=theater_id)

    def create(self, name, address, number_of_halls):
        theater = Theater(name=name, address=address, number_of_halls=number_of_halls)
        theater.save()
        return theater

    def update(self, theater_id, name, address, number_of_halls):
        try:
            theater = Theater.objects.get(id=theater_id)
            theater.name = name
            theater.address = address
            theater.number_of_halls = number_of_halls
            theater.save()
            return theater
        except Theater.DoesNotExist:
            raise ValueError(f"Theater with ID {theater_id} does not exist.")
