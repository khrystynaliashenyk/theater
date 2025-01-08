from theater_lab.models import Role

class RoleRepository:
    def get_all(self):
        return Role.objects.all()

    def get_by_id(self, role_id):
        return Role.objects.get(id=role_id)

    def create(self, role_name, actor, play):
        role = Role(role_name=role_name, actor=actor, play=play)
        role.save()
        return role