from theater_lab.models import Director

class DirectorRepository:
    def get_all(self):
        return Director.objects.all()

    def get_by_id(self, director_id):
        return Director.objects.get(id=director_id)

    def create(self, first_name, last_name, date_of_birth=None):
        director = Director(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
        director.save()
        return director

    def update(self, director_id, first_name, last_name, date_of_birth=None):
        try:
            director = Director.objects.get(id=director_id)
            director.first_name = first_name
            director.last_name = last_name
            director.date_of_birth = date_of_birth
            director.save()
            return director
        except Director.DoesNotExist:
            raise ValueError(f"Director with ID {director_id} does not exist.")
