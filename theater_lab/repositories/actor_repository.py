from theater_lab.models import Actor

class ActorRepository:
    def get_all(self):
        return Actor.objects.all()

    def get_by_id(self, actor_id):
        return Actor.objects.get(id=actor_id)

    def create(self, first_name, last_name, date_of_birth=None):
        actor = Actor(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth)
        actor.save()
        return actor